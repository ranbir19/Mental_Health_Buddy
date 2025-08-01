import gradio as gr
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Your Azure/OpenAI endpoint and model
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

# Directly add your GitHub token here (replace with your actual token)
token = "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"

# Initialize Azure client
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def ask_azure_gpt(message):
    response = client.complete(
        messages=[
            SystemMessage("You are a compassionate mental health assistant."),
            UserMessage(message),
        ],
        temperature=1,
        top_p=1,
        model=model
    )
    return response.choices[0].message.content

def respond(message, history):
    reply = ask_azure_gpt(message)
    return reply

# Launch Gradio chat interface
gr.ChatInterface(fn=respond, title="Mental Health Buddy").launch()
