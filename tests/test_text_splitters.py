
from services.rag.document_loader import DocumentLoader
from services.rag.text_splitter import textsplitter as TextSplitter 


def main():
    loader = DocumentLoader()
    splitter = TextSplitter()

    loaded_documents = loader.load_documents()
    split_documents = splitter.split_documents(loaded_documents)

    print(f"\nLoaded Documents : {len(loaded_documents)}")
    print(f"Split Documents  : {len(split_documents)}")

    print("\n")
    print("=" * 80)
    print(split_documents[0].page_content)


if __name__ == "__main__":
    main()