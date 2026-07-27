from app.retriever import search

query = "What is Retrieval Augmented Generation?"

results = search(query)

print("=" * 80)
print(f"Retrieved {len(results)} Documents")
print("=" * 80)

for i, doc in enumerate(results, start=1):

    print(f"\nResult {i}")

    print("-" * 60)

    print("Source :", doc.metadata["source"])
    print("Page   :", doc.metadata["page"])
    print("Paper  :", doc.metadata["paper_title"])

    print("\nPreview:\n")

    print(doc.page_content[:500])
