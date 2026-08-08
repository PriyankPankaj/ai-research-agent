import chromadb
from chromadb.utils import embedding_functions

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "research_documents"


class Retriever:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=CHROMA_PATH)
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            embedding_function=self.embedding_fn
        )

    def add_documents(self, documents: list[str], ids: list[str] = None):
        """Add raw text documents to the vector store."""
        if ids is None:
            ids = [f"doc_{i}" for i in range(len(documents))]
        self.collection.add(documents=documents, ids=ids)

    def query(self, query_text: str, n_results: int = 3) -> list[dict]:
        """Retrieve the most relevant documents for a query."""
        results = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        sources = []
        docs = results.get("documents", [[]])[0]
        distances = results.get("distances", [[]])[0]
        ids = results.get("ids", [[]])[0]

        for doc_id, doc_text, distance in zip(ids, docs, distances):
            sources.append({
                "id": doc_id,
                "content": doc_text,
                "relevance_score": 1 - distance,  # convert distance to similarity
            })
        return sources