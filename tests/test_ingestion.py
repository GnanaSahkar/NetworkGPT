
"""
Test the complete RAG ingestion pipeline.
"""

from services.rag import vector_store
from services.rag.document_loader import DocumentLoader
from services.rag.text_splitter import textsplitter as TextSplitter
from services.rag.embeddings import EmbeddingService
from services.rag.vector_store import VectorStore


def main():

    loader = DocumentLoader()
    splitter = TextSplitter()
    embedder = EmbeddingService()
    vector_store = VectorStore()

    # Load documents
    documents = loader.load_documents()
    print(f"Loaded Documents : {len(documents)}")

    # Split documents
    chunks = splitter.split_documents(documents)
    print(f"Split Documents : {len(chunks)}")

    # Generate embeddings
    embeddings = embedder.embed_documents(chunks)
    print(f"Generated Embeddings : {len(embeddings)}")

    # Store in ChromaDB
    vector_store.add_documents(
        documents=chunks,
        embeddings=embeddings,
    )

    print("Documents added successfully!")

    print(f"Collection Count : {vector_store.collection.count()}")
    print(f"Collection Name : {vector_store.collection.name}")
    


if __name__ == "__main__":
    main()