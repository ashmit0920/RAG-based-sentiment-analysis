from transformers import pipeline

# model_id = "meta-llama/Meta-Llama-3-8B"

# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForCausalLM.from_pretrained(model_id)

pipe = pipeline("sentiment-analysis") # defaults to distilbert llm

# out = pipe(inputs=["It was a bad store.", "It was a good store"])
# print(out)