from llmload import LoadLLM
import time

def chat(query : str):
    llm = LoadLLM()
    start = time.time()
    print("llm : ",llm)
    print("query : ",query)
    print("response :", llm(query))
    end = time.time()
    print("Response took : ", round(end - start) + " s.")
    return "DONE"