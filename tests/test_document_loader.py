
from services.rag.document_loader import DocumentLoader


def main():
    loader = DocumentLoader()

    loaded_documents = loader.load_documents()

    print("\n")
    print("=" * 80)
    print(f"Loaded Documents : {len(loaded_documents)}")
    print("=" * 80)

    for index, document in enumerate(loaded_documents, start=1):
        print(f"\nDocument {index}")
        print("-" * 50)
        print(document.metadata)
        print()
        print(document.page_content)


if __name__ == "__main__":
    main()