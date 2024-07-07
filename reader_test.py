from llama_index.core import SimpleDirectoryReader
from llama_index.core.llama_dataset import download_llama_dataset

rag_dataset, documents = download_llama_dataset("BlockchainSolanaDataset", "./data")
print(rag_dataset.to_pandas()[:5])

reader = SimpleDirectoryReader(input_files=["sample.txt"])

document = reader.load_data()

print(document)