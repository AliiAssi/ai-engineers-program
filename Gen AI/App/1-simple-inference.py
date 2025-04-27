import os
from dotenv import load_dotenv
from mistralai import Mistral
# Load environment variables
load_dotenv()
# print(os.getenv("MISTRAL_API_KEY"))
# Get the API key
api_key = os.getenv("MISTRAL_API_KEY")

# Initialize the Mistral client

client = Mistral(api_key=api_key)
# Create the chat messages
messages = [
    {"role": "system", "content": "You are a helpful assistant in football."},
    {"role": "user", "content": "Write a story about barcelona in 5 lines."}
]

# Generate the completion
response = client.chat.complete(
    model="mistral-large-latest", 
    messages=messages,
    temperature=0.3
)

# Print the response
print(f'Response: {response.choices[0].message.content}')
