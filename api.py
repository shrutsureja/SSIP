from ragFunction import rag
from GenerateQuestion import generateQuestion
from load_document import ingestDocument
from chatLLM import chat

while True:
    stage = input("\nEnter a stage: ")
    if stage == "ingest":
        print("Ingesting...")
        ingestDocument()
    elif stage == "question":
        print("Generating question...")
        generateQuestion()
    elif stage == "rag":
        print("Ask the Question...")
        while True:
            query = input("\nEnter a question: ")
            if query == "exit":
                print("Exiting... RAG")
                break
            else:
                ans = rag(query)
    elif stage == "chat":
        print("Chat with LLM...")
        while True:
            query = input("\nEnter a question: ")
            if query == "exit":
                print("Exiting... Chat")
                break
            else:
                ans = chat(query)
    elif stage == "exit":
        break
    else:
        print("Invalid stage")