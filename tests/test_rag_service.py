
from services.rag.rag_service import RAGService


def main():

    rag = RAGService()

    answer = rag.ask(
        "What is AAA?"
    )

    print("\n")
    print("=" * 80)
    print("NETWORKGPT RESPONSE")
    print("=" * 80)
    print(answer)


if __name__ == "__main__":
    main()