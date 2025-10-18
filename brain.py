import os
import google.generativeai as genai
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
import requests
from PIL import Image

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# --- GLOBAL VARIABLES ---
VECTOR_STORE_PATH = "artisan_marbles_db"
KNOWLEDGE_BASE_PATH = "knowledge_base"

# --- RAG KNOWLEDGE BASE SETUP ---
def get_vector_store():
    """Initializes and returns the Chroma vector store."""
    if os.path.exists(VECTOR_STORE_PATH):
        # Load existing vector store
        return Chroma(
            persist_directory=VECTOR_STORE_PATH,
            embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        )
    else:
        # Create a new one
        print("Creating new vector store...")
        loader = DirectoryLoader(KNOWLEDGE_BASE_PATH, glob="*.md", loader_cls=TextLoader)
        documents = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)
        
        vector_store = Chroma.from_documents(
            documents=texts,
            embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
            persist_directory=VECTOR_STORE_PATH
        )
        print("Vector store created.")
        return vector_store

vector_store = get_vector_store()
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# --- CONVERSATION MEMORY ---
# In a real app, this would be a database (like Redis). For a prototype, a simple dict is fine.
conversation_history = {}

# --- CORE CHATBOT MODELS & LOGIC ---
text_generation_model = genai.GenerativeModel('gemini-2.5-pro')
vision_model = genai.GenerativeModel('gemini-2.5-pro')

def get_rag_context(query):
    """Retrieves relevant context from the vector store."""
    docs = retriever.invoke(query)
    return "\n".join(doc.page_content for doc in docs)

def process_chat_message(user_phone, user_message, image_path=None):
    """
    The main function to handle user input (text or image) and generate a response.
    """
    global conversation_history
    
    # Retrieve or create conversation history for the user
    history = conversation_history.get(user_phone, [])
    
    # --- IMAGE ANALYSIS LOGIC ---
    if image_path:
        try:
            img = Image.open(image_path)
            image_analysis_prompt = '''
            You are a world-class interior designer for 'Artisan Marbles'.
            Analyze the user's uploaded image of their room. Consider the style (modern, classic, rustic), color palette, lighting, and existing furniture.
            Based on your analysis, suggest ONE specific marble from the context provided below that would be a perfect fit for a dining or tabletop in this space.
            Explain your choice in 2-3 sentences, linking it to the room's aesthetic.
            Do not offer to generate an image yet. Just provide the analysis and suggestion.
            
            CONTEXT:
            {rag_context} 
            '''
            rag_context = get_rag_context("Product descriptions of all marbles")
            prompt = image_analysis_prompt.format(rag_context=rag_context)
            
            response = vision_model.generate_content([prompt, img])
            bot_response = response.text

        except Exception as e:
            print(f"Error processing image: {e}")
            bot_response = "I'm sorry, I had trouble analyzing that image. Could you please try another one?"

    # --- TEXT-ONLY LOGIC ---
    else:
        # Check for lead capture intent
        if any(keyword in user_message.lower() for keyword in ["consultant", "speak to someone", "schedule a call"]):
             bot_response = "I can certainly help with that. To connect you with a design consultant, could you please provide your full name and email address?"
        
        else:
            rag_context = get_rag_context(user_message)
            
            prompt_template = '''
            You are Elea, an AI concierge for 'Artisan Marbles'. Your tone is elegant, helpful, and professional.
            Answer the user's question based on your conversation history and the context provided below.
            If the context doesn't have the answer, state that you may need to connect them with a design consultant for specific details.
            Do not make up information.

            CONVERSATION HISTORY:
            {history}

            CONTEXT:
            {rag_context}

            USER'S QUESTION:
            {user_message}

            YOUR RESPONSE:
            '''
            
            history_str = "\n".join([f"{msg['role']}: {msg['content']}" for msg in history])
            prompt = prompt_template.format(
                history=history_str,
                rag_context=rag_context,
                user_message=user_message
            )
            
            response = text_generation_model.generate_content(prompt)
            bot_response = response.text

    # Update conversation history
    history.append({"role": "user", "content": user_message})
    history.append({"role": "model", "content": bot_response})
    # Keep history from getting too long
    conversation_history[user_phone] = history[-10:] 

    return bot_response

def check_for_lead_details(message):
    """A simple check to see if a message might contain a name and email."""
    # This is a basic check. A more robust solution would use regex or NLP entity recognition.
    if '@' in message and len(message.split()) >= 2:
        # Assuming format "John Doe john.doe@example.com"
        parts = message.split()
        name = " ".join(part for part in parts if '@' not in part)
        email = next((part for part in parts if '@' in part), None)
        return name, email
    return None, None
