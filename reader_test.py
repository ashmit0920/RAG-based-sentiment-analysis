from llama_index.core import SimpleDirectoryReader
from transformers import AutoTokenizer, pipeline
# from llama_index.core.llama_dataset import download_llama_dataset
import os

# rag_dataset, documents = download_llama_dataset("BlockchainSolanaDataset", "./data")
# print(rag_dataset.to_pandas()[:5])

def get_additional_context():
    reader = SimpleDirectoryReader(input_files=["sample_reviews.pdf"])

    document = reader.load_data()
    review_list = document[0].text.split("\n")
    additional_context = ",".join(review_list) # returns comma separated labelled reviews to feed into LLM
    # print(additional_context)
    return additional_context

def get_reviews():
    reader = SimpleDirectoryReader(input_files=["reviews.csv"])
    document = reader.load_data()
    review_list = document[0].text.split("\n") 
    reviews = " ".join(review_list) # returns a paragraph of all reviews that can be summarised by the bart pipeline
    return reviews

model = "facebook/bart-large-cnn"
# model = "openai-community/gpt2"
tokenizer = AutoTokenizer.from_pretrained(model)

sentiment_pipe = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

reviews = get_reviews()
summary = summarizer(reviews, min_length=5, max_length=50)
print(summary)
# print(get_reviews())