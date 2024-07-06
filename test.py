from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import transformers

# Add caching directory to save storage
# Use Ollama with llama index -> https://docs.llamaindex.ai/en/stable/examples/llm/ollama/

model_id = "meta-llama/Meta-Llama-3-8B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

pipeline = transformers.pipeline(
    "text-generation", model=model_id, tokenizer=model_id, use_auth_token=True
)
pipeline("Hey how are you doing today?")


def analyze_sentiment_llm(feedback_texts):
    sentiment_results = []
    for text in feedback_texts:
        inputs = tokenizer(f"Analyze the sentiment of this text: {text}", return_tensors="pt")
        outputs = model.generate(**inputs, max_length=50)
        sentiment = tokenizer.decode(outputs[0], skip_special_tokens=True)
        sentiment_results.append(sentiment.strip())
    return sentiment_results

analyze_sentiment_llm(["This is a positive feedback.", "This is a negative feedback."])