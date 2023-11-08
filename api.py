from ragFunction import rag
from GenerateQuestion import generateQuestion

while True:
    stage = input("\nEnter a stage: ")
    if stage == "ingest":
        print("Ingesting...")
    elif stage == "question":
        print("Generating question...")
        generateQuestion()
    elif stage == "rag":
        print("Ask the Question...")
        query = input("\nEnter a question: ")
        ans = rag(query)
    elif stage == "exit":
        break