from langchain.llms import LlamaCpp

from dotenv import load_dotenv
import os

if not load_dotenv():
    print("Could not load .env file or it is empty. Please check if it exists and is readable.")
    exit(1)
    
model_path = os.environ.get('MODEL_PATH')
llm = None

def LoadLLM(**kwargs):
    global llm
    if llm is None:
        llm = LlamaCpp(model_path="model", **kwargs)
    return llm