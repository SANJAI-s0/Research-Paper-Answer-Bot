from app.rag_chain import ask

question = "Explain Retrieval-Augmented Generation."

answer, sources = ask(question)

print("=" * 80)
print("QUESTION")
print("=" * 80)
print(question)

print("\n")

print("=" * 80)
print("ANSWER")
print("=" * 80)
print(answer)

print("\n")

print("=" * 80)
print("SOURCES")
print("=" * 80)

for paper, pages in sources.items():
    page_list = ", ".join(map(str, sorted(pages)))
    print(f"{paper} (Pages: {page_list})")
