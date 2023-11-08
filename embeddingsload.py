from dotenv import load_dotenv

import os 

if not load_dotenv():
    print("Could not load .env file or it is empty. Please check if it exists and is readable.")
    exit(1)

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")

from langchain.embeddings import HuggingFaceInstructEmbeddings

def LoadEmbeddings():
    return HuggingFaceInstructEmbeddings(model_name=embeddings_model_name)