from huggingface_hub import login
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from llama_index.core.llms import ChatMessage
import ollama
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

# login(token=TOKEN)

llm = HuggingFaceInferenceAPI(model_name = "google/gemma-2-9b", token = TOKEN)

# ollama_client = ollama.Client()

response = llm.chat([ChatMessage(role="user", content="Hello, What is Gemma?")])
print(response.content)
