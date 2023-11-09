from llmload import LoadLLM
import time

def chat(query : str):
    # llm = LoadLLM(temperature: 0.8, top_p: 0.95, repeat_penalty: 1.1, top_k: 40, n_ctx: 1024, n_batch: 8, n_gpu_layers: 90, verbose: False)
    llm = LoadLLM(n_ctx=1024, n_batch=8, verbose=False ,n_gpu_layers = 90, temperature=0.8, top_p=0.95, repeat_penalty=1.1, top_k=40)
    start = time.time()
    print("llm : ",llm)
    print("query : ",query)
    res = llm(query)
    print("response :", res)
    end = time.time()
    print(f"Response took : {round(end - start)} s.")
    return res,round(end - start)