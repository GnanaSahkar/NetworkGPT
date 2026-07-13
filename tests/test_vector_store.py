
from services.rag.vector_store import VectorStore


def main():

    store = VectorStore()

    print("Collection Name :", store.collection.name)

    print("Document Count :", store.collection.count())


if __name__ == "__main__":
    main()