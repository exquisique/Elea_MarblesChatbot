# Elea - The Artisan Marbles Chatbot

This is a WhatsApp chatbot named Elea, built for an imaginary company called Artisan Marbles. Elea is designed to handle customer queries about products, pricing, and other company-related information. It leverages a Retrieval-Augmented Generation (RAG) architecture to provide accurate and contextually relevant answers.

## Features

*   **Conversational AI:** Engages users in a natural and helpful conversation on WhatsApp.
*   **RAG-based Knowledge:** Answers questions based on a knowledge base of markdown files.
*   **Product Recommendations:** Can analyze images of rooms sent via WhatsApp and recommend suitable marble products.
*   **Lead Capture:** Identifies when a user wants to speak to a consultant and captures their contact information.

## How it Works

This chatbot uses the Twilio API for WhatsApp. Here's how it works:

1.  A user sends a message to the designated Artisan Marbles WhatsApp number.
2.  Twilio receives the message and forwards it to a webhook URL, which is handled by this Flask application.
3.  The Flask application processes the message with Elea, the RAG-based chatbot.
4.  Elea generates a response, which is sent back to the user on WhatsApp through the Twilio API.

## Getting Started

### Prerequisites

*   Python 3.7+
*   Git
*   A Twilio account with a WhatsApp-enabled phone number

### Installation

1.  **Clone the repository:**
    ```
    git clone https://github.com/exquisique/Elea_MarblesChatbot.git
    ```

2.  **Create a virtual environment:**
    ```
    python -m venv Env
    source Env/bin/activate  # On Windows, use `Env\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```
    pip install -r requirements.txt
    ```

4.  **Set up your environment variables:**
    Create a file named `.env` in the root of the project and add your Google API key and Twilio credentials:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY"
    TWILIO_ACCOUNT_SID="YOUR_TWILIO_ACCOUNT_SID"
    TWILIO_AUTH_TOKEN="YOUR_TWILIO_AUTH_TOKEN"
    ```

### Running the Application

To start the chatbot, run the following command:

```
python app.py
```

You will also need to expose your local server to the internet so that Twilio can send webhooks to it. A tool like `ngrok` can be used for this.

## Usage

Once the application is running and your Twilio webhook is configured, you can interact with Elea by sending messages to your Twilio WhatsApp number. You can ask questions about Artisan Marbles' products, pricing, or company information. You can also send images of rooms to get product recommendations.
