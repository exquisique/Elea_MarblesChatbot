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
