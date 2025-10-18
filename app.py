import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import requests
from dotenv import load_dotenv

# Import our custom modules
from brain import process_chat_message, check_for_lead_details
from utils import save_lead

# --- INITIALIZATION ---

# Load environment variables from the .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Initialize the Twilio Client for sending messages
try:
    twilio_client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
except Exception as e:
    print(f"Error initializing Twilio client: {e}")
    print("Please ensure TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN are set in your .env file.")
    twilio_client = None


# --- HELPERS ---

# A mapping from MIME types (provided by Twilio) to common file extensions
# This is the key fix for the image identification issue.
MIME_TYPE_MAP = {
    'image/jpeg': '.jpg',
    'image/png': '.png',
    'image/gif': '.gif',
    'image/webp': '.webp',
}


# --- WEBHOOK FOR INCOMING MESSAGES ---

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    This function is the main entry point for all incoming WhatsApp messages
    forwarded by Twilio.
    """
    
    # Parse the essential data from the incoming Twilio request
    incoming_msg = request.values.get('Body', '').strip()
    from_number = request.values.get('From', '')
    
    print(f"Incoming message from {from_number}: '{incoming_msg}'")
    
    # --- LOGIC FLOW ---

    # 1. First, check if the message contains lead details (name and email)
    name, email = check_for_lead_details(incoming_msg)
    if name and email:
        # If it's a lead, save it and send a confirmation message
        save_lead(from_number, name, email)
        bot_response = "Thank you. A design consultant will be in touch with you shortly. Is there anything else I can help you with today?"
    else:
        # 2. If it's not a lead, process it as a regular chat message (text or image)
        image_path = None
        
        # Check if the incoming message includes an image
        if 'MediaUrl0' in request.values:
            media_url = request.values.get('MediaUrl0')
            
            # Get the image type (e.g., 'image/jpeg') and determine the correct file extension
            content_type = request.values.get('MediaContentType0', 'application/octet-stream')
            file_extension = MIME_TYPE_MAP.get(content_type, '.jpg') # Default to .jpg if type is unknown
            
            # Create a unique filename and path
            base_filename = media_url.split('/')[-1]
            filename = os.path.join('downloads', base_filename + file_extension)
            
            try:
                # Download the image from the Twilio URL and save it locally
                with open(filename, 'wb') as f:
                    image_data = requests.get(media_url, auth=(twilio_client.username, twilio_client.password)).content
                    f.write(image_data)
                image_path = filename
                print(f"Image downloaded successfully to: {image_path}")
            except Exception as e:
                print(f"Failed to download or save image: {e}")
                image_path = None # Ensure image_path is None if download fails
        
        # Pass the message (and image path, if any) to the AI brain for processing
        bot_response = process_chat_message(from_number, incoming_msg, image_path)

        # Clean up by deleting the temporary image file after processing
        if image_path and os.path.exists(image_path):
            #os.remove(image_path)
            print(f"Cleaned up image file: {image_path}")

    # --- SEND THE REPLY ---
    
    # Use Twilio's helper library to construct a valid WhatsApp reply
    twiml_response = MessagingResponse()
    twiml_response.message(bot_response)
    
    return str(twiml_response)


# --- MAIN EXECUTION BLOCK ---

if __name__ == '__main__':
    # Ensure the 'downloads' directory exists before starting the app
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
        print("Created 'downloads' directory.")
        
    # Start the Flask development server
    # debug=True provides helpful error messages but should be turned off for production
    app.run(port=5000, debug=True)