from app.loader import load_documents
from app.chunking import chunk_documents

docs = load_documents()
chunks = chunk_documents(docs)

print("=" * 60)
print("Original Pages :", len(docs))
print("Total Chunks   :", len(chunks))
print("=" * 60)

print("\nChunk Metadata:\n")
print(chunks[0].metadata)

print("\nChunk Preview:\n")
print(chunks[0].page_content[:700])

chunk_lengths = [len(chunk.page_content) for chunk in chunks]

print("\nChunk Statistics")
print("-" * 30)
print("Minimum :", min(chunk_lengths))
print("Maximum :", max(chunk_lengths))
print("Average :", round(sum(chunk_lengths) / len(chunk_lengths), 2))
