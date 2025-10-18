import os
import csv
import time
from dotenv import load_dotenv
from twilio.rest import Client

# --- SETUP AND CONFIGURATION ---
# Load all the secret keys from our .env file
load_dotenv()

# Get Twilio credentials from the environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER") # This is your Twilio Sandbox number

# --- SANDBOX CAMPAIGN DETAILS ---
# We will fill the pre-approved template: "Your {{1}} code is {{2}}"
CAMPAIGN_NAME = "festive first look at the new Artisan Marbles collection! ✨ To celebrate Diwali, new clients receive 10% off their first order. Your exclusive preview"

# {{2}} WELCOME_CODE: This is our culturally relevant and memorable code.
WELCOME_CODE = "SHUBH-LABH"


def send_sandbox_message(customer_name, customer_number):
    """Sends a message using the pre-approved Twilio Sandbox template."""
    try:
        twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        # We must construct the body to EXACTLY match the sandbox template structure.
        # The template is: "Your {{1}} code is {{2}}"
        template_body = f"Your {CAMPAIGN_NAME} code is {WELCOME_CODE}"
        
        print(f"Sending sandbox message to {customer_name} at {customer_number}...")
        print(f"  -> Message body: '{template_body}'")
        
        # For the sandbox, we send a 'body' that matches the template.
        # Twilio recognizes the structure and lets it through.
        message = twilio_client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            to=customer_number,
            body=template_body
        )
        
        print(f"  -> Success! Message SID: {message.sid}")
        return True
        
    except Exception as e:
        # Twilio errors are helpful. Let's print the full error.
        print(f"  -> FAILED to send to {customer_name}. Twilio Error: {e}")
        return False


if __name__ == "__main__":
    print("--- Artisan Marbles Sandbox Campaign Sender ---")
    
    try:
        with open('opted_in_customers.csv', mode='r', encoding='utf-8') as infile:
            customers = list(csv.DictReader(infile))
    except FileNotFoundError:
        print("\nERROR: Could not find 'opted_in_customers.csv'. Please create it.\n")
        exit()

    if not customers:
        print("\nERROR: No customers found in the CSV file.\n")
        exit()

    print(f"Found {len(customers)} customer(s) for this campaign.")
    
    success_count = 0
    failure_count = 0

    for customer in customers:
        if send_sandbox_message(customer['FirstName'], customer['WhatsAppNumber']):
            success_count += 1
        else:
            failure_count += 1
        
        time.sleep(1) # Wait 1 second between messages

    print("\n--- Campaign Complete ---")
    print(f"Messages sent successfully: {success_count}")
    print(f"Messages failed: {failure_count}")