from dotenv import load_dotenv
from mistralai import Mistral
import gradio as gr
import os
# Load environment variables
load_dotenv()
# print(os.getenv("MISTRAL_API_KEY"))
# Get the API key
api_key = os.getenv("MISTRAL_API_KEY")

# Initialize the Mistral client

client = Mistral(api_key=api_key)


def chat_with_model(history, new_message):
    messages = [{"role" : "system" , "content" : "You are a helpful assistant."}]
    for user_message, assistant_response in history:
        messages.append({"role" : "user" , "content" : user_message})
        messages.append({"role" : "assistant" , "content" : assistant_response})
    
    messages.append({"role" : "user" , "content" : new_message})

    response = client.chat.complete(
    model="mistral-large-latest", 
    messages=messages,
    temperature=0.3
    )

    assistant_message = response.choices[0].message.content
    history.append((new_message,assistant_message))
    return history , ""
        

def gradio_chat_app():
    with gr.Blocks() as app:
        gr.Markdown("# Mistral Chatbot")
        gr.Markdown("Chat with the Phi model in a conversational format.")
        
        chatbot = gr.Chatbot(label = "Chat Interface")
        user_input = gr.Textbox(label = "your message" , placeholder = "Type something ..." , lines=1)  
        send_button = gr.Button("send")
        
        def clear_chat():
            return [] , ""
    
        clear_button = gr.Button("Clear chat")
        
        send_button.click(
            fn=chat_with_model, 
            inputs = [chatbot, user_input],
            outputs = [chatbot, user_input]
        )
        clear_button.click(
            fn=clear_chat,
            inputs = [],
            outputs = [chatbot, user_input]
        )
        
    return app


if __name__ == "__main__":
    app = gradio_chat_app()
    app.launch()