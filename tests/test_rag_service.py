"""
Test the RAG Service.
"""

from services.rag.rag_service import RAGService


def main():
    rag = RAGService()

    query = "Cisco OSPF router-id configuration"

    print("=" * 80)
    print("RETRIEVED CONTEXT")
    print("=" * 80)

    context = rag.retrieve_context(
        query=query,
    )

    print(context)

    print("\n")
    print("=" * 80)
    print("AI RESPONSE")
    print("=" * 80)

    answer = rag.ask(
        question=query,
    )

    print(answer)


if __name__ == "__main__":
    main()