from huggingface_hub import login
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from llama_index.core.llms import ChatMessage
# import ollama
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

# login(token=TOKEN)

llm = HuggingFaceInferenceAPI(model_name = "microsoft/Phi-3-mini-128k-instruct") # token = TOKEN)

# ollama_client = ollama.Client()

response = llm.chat([ChatMessage(role="user", content="Hello, What is microsoft?")])
print(response.content)
