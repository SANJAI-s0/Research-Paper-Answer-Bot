from app.loader import load_documents

docs = load_documents()

print("=" * 60)
print("Total Pages:", len(docs))
print("=" * 60)

print("\nMetadata Example:\n")
print(docs[0].metadata)

print("\nPreview:\n")
print(docs[0].page_content[:600])
