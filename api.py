from ragFunction import rag

while True:
    query = input("\nEnter a query: ")
    if query == "exit":
        break
    if query.strip() == "":
        continue
    ans = rag(query)
