import time

from app.config import EVALUATION_QUERIES
from app.rag_chain import ask

print("=" * 80)
print("Research Paper Answer Bot Evaluation")
print("=" * 80)

results = []

for i, question in enumerate(EVALUATION_QUERIES, start=1):

    print(f"\nQuery {i}")
    print("-" * 80)
    print(question)

    start = time.time()

    result = ask(question)

    elapsed = time.time() - start

    print(f"\nResponse Time : {elapsed:.2f} sec")

    print("\nRetrieved Papers:")

    for paper, pages in result["sources"].items():
        print(f"  • {paper} (Pages: {pages})")

    print("\nGenerated Answer Preview:")
    print(result["answer"][:250] + "...")

    results.append(
        {
            "query": question,
            "time": elapsed,
            "papers": len(result["sources"]),
        }
    )

print("\n" + "=" * 80)
print("Summary")
print("=" * 80)

avg = sum(r["time"] for r in results) / len(results)

print(f"Average Response Time : {avg:.2f} sec")
print(f"Total Queries Tested  : {len(results)}")
