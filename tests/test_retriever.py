
from services.rag.retriever import Retriever


def main():

    retriever = Retriever()

    results = retriever.retrieve(
        query="What is AAA?",
        top_k=3,
    )

    print(results)


if __name__ == "__main__":
    main()