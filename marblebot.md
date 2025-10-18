Of course. This is an ambitious and exciting project. Let's build a professional, sophisticated WhatsApp chatbot prototype for "Artisan Marbles" step-by-step.

This guide will give you everything you need: the project structure, the complete code for each file, a comprehensive dataset, and instructions on how to run it.

First, let's set up your professional repository structure.

### **Step 1: Project Structure**

In VS Code, create a new project folder (e.g., `marble_chatbot`) and structure it exactly like this. This clean separation of concerns is crucial for a professional project.

```
/marble_chatbot/
|
|-- /knowledge_base/
|   |-- 01_products.md
|   |-- 02_pricing_and_customization.md
|   |-- 03_faq.md
|   |-- 04_company_info.md
|
|-- /downloads/
|   |-- (This folder will store user-uploaded images temporarily)
|
|-- app.py                 # Flask Server & Twilio Webhook Logic
|-- brain.py               # Core Chatbot Logic (RAG, Gemini, Skills)
|-- utils.py               # Helper functions (e.g., lead saving)
|-- requirements.txt       # List of all Python libraries needed
|-- .env                   # To store your secret API keys
|-- .gitignore             # To exclude unnecessary files from version control
```

---

### **Step 2: Create the Extensive Imaginary Dataset**

Create the `knowledge_base` folder. Inside it, create the four markdown files below. This is the "brain" of your RAG system.

#### `01_products.md`
```markdown
# Artisan Marbles Product Catalog

## Premium Tier Marbles

### Calacatta Gold
- **Origin:** Carrara, Italy
- **Description:** The epitome of luxury. Calacatta Gold is celebrated for its bright white background and its thick, dramatic veining in shades of grey and gold. Each slab is a unique piece of art.
- **Best For:** Statement dining tables, luxury kitchen islands, high-impact feature walls.
- **Properties:** It is a softer, more porous marble, requiring diligent sealing and care. Best for lower-traffic, high-visibility areas.
- **Available Shapes:** Rectangular, Round, Oval, Custom.

### Statuario
- **Origin:** Carrara, Italy
- **Description:** Prized for its stark white background—whiter than Carrara—with fewer, but more dramatic and distinct grey veins. It has a classic, clean, and breathtaking look.
- **Best For:** Sculptural dining tables, minimalist and modern designs, bathroom vanities.
- **Properties:** Similar in porosity to Calacatta, it demands respect and proper care to maintain its pristine beauty.
- **Available Shapes:** Rectangular, Round.

## Standard Tier Marbles

### Carrara
- **Origin:** Carrara, Italy
- **Description:** The classic Italian marble. Carrara is known for its softer, more subtle appearance, with a light grey base and fine, feathery grey veining. It's timeless and versatile.
- **Best For:** Any application, from kitchen tabletops to coffee tables. A durable and popular choice.
- **Properties:** It is more forgiving than Calacatta or Statuario but still requires sealing. Its softer look can hide minor etching better.
- **Available Shapes:** Rectangular, Round, Oval, Square.

### Nero Marquina
- **Origin:** Basque Country, Spain
- **Description:** A striking, deep black marble with distinctive white lightning-like veins. It offers a powerful, modern, and sophisticated aesthetic.
- **Best For:** Coffee tables, side tables, and dining tables in modern or art-deco settings. Creates a stunning contrast.
- **Properties:** A dense and durable marble. The polished finish shows fingerprints and smudges more easily, so a honed finish is also popular.
- **Available Shapes:** Rectangular, Round, Square.

## Exotic Tier Marbles

### Verde Guatemala
- **Origin:** Guatemala
- **Description:** A rich, deep green marble with varying shades and dark veining, reminiscent of a lush forest. It's a bold and unique choice that brings nature indoors.
- **Best For:** Unique dining tables, bar tops, and accent tables.
- **Properties:** It's technically a serpentinite, making it more resistant to acids and etching than many lighter marbles.
- **Available Shapes:** Round, Custom.
```

#### `02_pricing_and_customization.md`
```markdown
# Artisan Marbles Pricing and Customization Guide

## Pricing Formula
The final price of a tabletop is calculated as:
(Area in Sq. Ft. * Price per Sq. Ft.) + (Perimeter in Linear Ft. * Edge Profile Cost) + Finish Cost

## Marble Price Tiers (Price per Square Foot)
- **Standard Tier (Carrara, Nero Marquina):** $85 per sq. ft.
- **Premium Tier (Calacatta Gold, Statuario):** $190 per sq. ft.
- **Exotic Tier (Verde Guatemala):** $135 per sq. ft.

## Edge Profiles (Price per Linear Foot)
- **Eased Edge (Standard):** Included in base price ($0)
- **Bullnose (Rounded):** $20 per linear ft.
- **Ogee (Decorative S-shape):** $35 per linear ft.

## Finishes
- **Polished (Glossy):** Included in base price.
- **Honed (Matte):** $15 per sq. ft. additional cost. This finish is less reflective and has a soft, satin feel. It can help hide minor scratches and etching.

## Table Bases
We offer a range of bases that are priced separately.
- **Matte Black Steel Pedestal:** $450
- **Polished Brass Cylinder:** $700
- **Solid Oak Trestle:** $850

## Example Calculation
For a 6 ft by 3 ft rectangular Carrara table with a Bullnose edge and Polished finish:
- Area: 6 * 3 = 18 sq. ft.
- Perimeter: (6 + 3) * 2 = 18 linear ft.
- Marble Cost: 18 sq. ft. * $85/sq. ft. = $1530
- Edge Cost: 18 linear ft. * $20/linear ft. = $360
- Finish Cost: $0 (Polished is included)
- **Total Tabletop Cost: $1530 + $360 = $1890**
```

#### `03_faq.md`
```markdown
# Artisan Marbles - Frequently Asked Questions

**Q: How do I clean my marble table?**
A: For daily cleaning, use a soft cloth with warm water and a pH-neutral stone cleaner. Wipe up spills, especially acidic ones like wine, coffee, or citrus juice, immediately. Do not use vinegar, Windex, or bleach, as they will etch the surface.

**Q: Will my marble table stain?**
A: Marble is a porous natural stone. We apply a high-grade sealant to all our products before delivery, which provides significant protection against staining. However, spills left for a long time can still penetrate. We recommend reapplying a sealant once a year.

**Q: Is marble heat resistant? Can I put a hot pan on it?**
A: While marble doesn't burn, it is susceptible to "thermal shock," which can cause cracks or discoloration. We strongly recommend always using trivets or mats for hot pots and pans.

**Q: What is the difference between a "honed" and "polished" finish?**
A: A polished finish is glossy, reflective, and enhances the stone's color and veining. A honed finish is matte, with a soft, satin feel. Honed finishes are more resistant to showing scratches and are increasingly popular for a modern look, but they can be slightly more susceptible to showing stains if not sealed properly.

**Q: What is your lead time for a custom table?**
A: Our standard lead time is 6-8 weeks from order confirmation to delivery. This can vary based on the complexity of the project and the availability of the chosen slab.

**Q: What is your return policy?**
A: As each piece is custom-made to your specifications, we cannot accept returns or cancellations once the production has begun. We will, of course, address any issues related to damage during shipping or manufacturing defects.
```

#### `04_company_info.md`
```markdown
# About Artisan Marbles

## Our Story
Founded on a passion for timeless natural materials, Artisan Marbles brings the world's most beautiful stone into your home. We are a family-owned business dedicated to craftsmanship, quality, and personalized service. We source our slabs directly from the finest quarries in Italy, Spain, and beyond.

## Our Process
Our process is a blend of traditional artisanship and modern technology. From digital templating to precision waterjet cutting and hand-finishing, every step is handled with care by our expert team.

## Contact Us
- To speak with a design consultant, please ask me to "schedule a consultation" and provide your contact details.
- For other inquiries, you can email us at contact@artisanmarbles.example.com.
- Our showroom is located at 123 Stone Cutter's Lane, and visits are by appointment only.
```

---

### **Step 3: Dependencies and Environment Setup**

Create the following two files in your root project directory.

#### `requirements.txt`
```
flask
twilio
python-dotenv
google-generativeai
langchain-google-genai
langchain
chromadb
langchain-community
requests
pypdf
unstructured
```

#### `.env`
Open this file and add your secret keys. **Never share this file.**
```
# Google AI API Key
GOOGLE_API_KEY="YOUR_GOOGLE_AI_API_KEY"

# Twilio Credentials
TWILIO_ACCOUNT_SID="YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN="YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER="whatsapp:+14155238886" # This is Twilio's sandbox number. Change it later to your own number.

# A secret key for your Flask app
FLASK_SECRET_KEY="generate_a_random_string_for_this"
```

#### `.gitignore`
This tells Git (version control) to ignore sensitive or unnecessary files.
```
# Environment variables
.env

# Python artifacts
__pycache__/
*.pyc

# Local data
/downloads/
/artisan_marbles_db/
leads.csv
```

---

### **Step 4: The Code**

Now, let's write the Python code for the three main files.

#### `utils.py`
This file will hold our helper function for saving leads.
```python
import csv
from datetime import datetime
import os

LEADS_FILE = 'leads.csv'

def save_lead(phone_number, name, email):
    """Appends a new lead to the CSV file."""
    
    # Check if the file exists, if not, create it with a header
    file_exists = os.path.isfile(LEADS_FILE)
    
    with open(LEADS_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(['Timestamp', 'PhoneNumber', 'Name', 'Email']) # Header
            
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, phone_number, name, email])
        
    print(f"Lead saved for {name}.")
    return True
```

#### `brain.py`
This is the most complex file. It contains all the AI logic.

```python
import os
import google.generativeai as genai
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
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
text_generation_model = genai.GenerativeModel('gemini-pro')
vision_model = genai.GenerativeModel('gemini-pro-vision')

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
            image_analysis_prompt = """
            You are a world-class interior designer for 'Artisan Marbles'.
            Analyze the user's uploaded image of their room. Consider the style (modern, classic, rustic), color palette, lighting, and existing furniture.
            Based on your analysis, suggest ONE specific marble from the context provided below that would be a perfect fit for a dining or tabletop in this space.
            Explain your choice in 2-3 sentences, linking it to the room's aesthetic.
            Do not offer to generate an image yet. Just provide the analysis and suggestion.
            
            CONTEXT:
            {rag_context}
            """
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
            
            prompt_template = """
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
            """
            
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

```

#### `app.py`
This is the web server that connects Twilio to your `brain`.

```python
import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import requests
from dotenv import load_dotenv

from brain import process_chat_message, check_for_lead_details
from utils import save_lead

# --- INITIALIZATION ---
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Twilio Client
twilio_client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")

# --- WEBHOOK FOR INCOMING MESSAGES ---
@app.route('/webhook', methods=['POST'])
def webhook():
    """Handles incoming messages from Twilio."""
    
    # Parse incoming data
    incoming_msg = request.values.get('Body', '').strip()
    from_number = request.values.get('From', '')
    
    print(f"Incoming message from {from_number}: {incoming_msg}")
    
    # --- Check for Lead Capture ---
    # A simple state check could be implemented here for more robust lead capture flow
    name, email = check_for_lead_details(incoming_msg)
    if name and email:
        save_lead(from_number, name, email)
        bot_response = "Thank you. A design consultant will be in touch with you shortly. Is there anything else I can help you with?"
    else:
        # --- Image Handling ---
        image_path = None
        if 'MediaUrl0' in request.values:
            media_url = request.values.get('MediaUrl0')
            try:
                # Download the image
                filename = os.path.join('downloads', media_url.split('/')[-1])
                with open(filename, 'wb') as f:
                    image_data = requests.get(media_url).content
                    f.write(image_data)
                image_path = filename
                print(f"Image downloaded to {image_path}")
            except Exception as e:
                print(f"Failed to download image: {e}")
        
        # Process the message (text or image) using the brain
        bot_response = process_chat_message(from_number, incoming_msg, image_path)

        # Clean up downloaded image
        if image_path and os.path.exists(image_path):
            os.remove(image_path)

    # --- Send the Reply ---
    twiml_response = MessagingResponse()
    twiml_response.message(bot_response)
    
    return str(twiml_response)

# --- MAIN EXECUTION ---
if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(port=5000, debug=True)

```
*Note on Image Generation:* The step of generating a new image with the table placed in the user's room is an advanced "in-painting" task. For this prototype, Elea will analyze the room and suggest the marble. A Phase 2 could involve sending the image and the suggestion to a specialized model like DALL-E 2's API or Google's Imagen via Vertex AI, which have explicit in-painting features.

---

### **Step 5: How to Run Everything**

1.  **Install Dependencies:**
    Open your terminal in the `marble_chatbot` directory and run:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Fill in your `.env` file:**
    Get your API keys from Google AI Studio, Twilio Console, and generate a random string for the Flask key.

3.  **Run the Initial RAG Indexing:**
    The first time you run the app, the vector store will be created. In your terminal, start the Flask server:
    ```bash
    python app.py
    ```
    You will see a message "Creating new vector store...". This will create the `artisan_marbles_db` folder. You can stop the server after you see "Vector store created." for the first time.

4.  **Expose Your Server with Ngrok:**
    Your Flask app is running on `localhost:5000`, which the internet can't see. We need ngrok.
    *   Download and set up ngrok.
    *   In a **new terminal window**, run:
        ```bash
        ngrok http 5000
        ```
    *   Ngrok will give you a public "Forwarding" URL (e.g., `https://1a2b-3c4d-5e6f.ngrok.io`). **Copy this URL.**

5.  **Configure the Twilio Sandbox for WhatsApp:**
    *   Log into your Twilio account.
    *   Navigate to "Messaging" -> "Try it out" -> "Send a WhatsApp message".
    *   Follow the instructions to connect to the sandbox by sending a code from your personal WhatsApp to Twilio's number.
    *   Go to the "Sandbox settings" tab.
    *   In the box labeled "WHEN A MESSAGE COMES IN", paste your ngrok URL and add `/webhook` to the end (e.g., `https://1a2b-3c4d-5e6f.ngrok.io/webhook`).
    *   Make sure the method is set to `HTTP POST`.
    *   Click "Save".

6.  **Start and Test:**
    *   Make sure your Flask server is running in the first terminal (`python app.py`).
    *   Make sure ngrok is running in the second terminal.
    *   Send a message from your WhatsApp to the Twilio number.

You can now talk to Elea, send it a picture of your room, ask it for quotes, and schedule a consultation. The entire workflow is now active.