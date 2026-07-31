"""
download_papers.py
------------------

Downloads all research papers required for the
Research Paper Answer Bot project.

Usage
-----
python download_papers.py
"""

from pathlib import Path
from urllib.request import urlretrieve

PAPER_DIR = Path("data/raw_papers")
PAPER_DIR.mkdir(parents=True, exist_ok=True)

PAPERS = {
    "attention.pdf":
        "https://arxiv.org/pdf/1706.03762.pdf",

    "bert.pdf":
        "https://arxiv.org/pdf/1810.04805.pdf",

    "gpt3.pdf":
        "https://arxiv.org/pdf/2005.14165.pdf",

    "rag.pdf":
        "https://arxiv.org/pdf/2005.11401.pdf",

    "react.pdf":
        "https://arxiv.org/pdf/2210.03629.pdf",

    "llama.pdf":
        "https://arxiv.org/pdf/2302.13971.pdf",

    "llama2.pdf":
        "https://arxiv.org/pdf/2307.09288.pdf",

    "instructgpt.pdf":
        "https://arxiv.org/pdf/2203.02155.pdf",

    "selfrag.pdf":
        "https://arxiv.org/pdf/2310.11511.pdf",

    "cot.pdf":
        "https://arxiv.org/pdf/2201.11903.pdf",
}


def download_file(name: str, url: str):

    destination = PAPER_DIR / name

    if destination.exists():
        print(f"[✓] {name} already exists.")
        return

    print(f"Downloading {name}...")

    try:

        urlretrieve(url, destination)

        print(f"[✓] Downloaded {name}")

    except Exception as e:

        print(f"[✗] Failed : {name}")

        print(e)


def main():

    print("=" * 60)
    print("Research Paper Downloader")
    print("=" * 60)

    for name, url in PAPERS.items():
        download_file(name, url)

    print("\nDone.")
    print(f"Papers saved in:\n{PAPER_DIR.resolve()}")


if __name__ == "__main__":
    main()
