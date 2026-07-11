from services.rag.embeddings import EmbeddingService

def main():
    embedding_service = EmbeddingService()

    response = embedding_service.client.models.embed_content(
        model=embedding_service.model,
        contents="AAA authentication using RADIUS"
    )

    print(type(response))
    print()
    print(response)


if __name__ == "__main__":
    main()