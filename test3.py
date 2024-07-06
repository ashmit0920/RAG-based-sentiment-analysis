from huggingface_hub import login
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from llama_index.core.llms import ChatMessage
import ollama
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN") # Hugging Face token to access restricted models (Llama 3)

# login(token=TOKEN)

llm = HuggingFaceInferenceAPI(model_name = "meta-llama/Meta-Llama-3-8B", token = TOKEN)

# ollama_client = ollama.Client()

response = llm.chat([ChatMessage(role="user", content="Hello, What is Llama 3?")])
print(response.content)