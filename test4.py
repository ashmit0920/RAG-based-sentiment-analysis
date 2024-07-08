from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model)

sentiment_pipe = pipeline("sentiment-analysis") # defaults to distilbert llm
summary_pipe = pipeline("summarization", model=model, tokenizer=tokenizer)

# out = pipe(inputs=["It was a bad store.", "It was a good store"])
# print(out)