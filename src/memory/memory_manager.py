import chromadb
from chromadb.utils import embedding_functions
from datetime import datetime, timezone
import uuid

MEMORY_DB_PATH = "chroma_db"
MEMORY_COLLECTION = "long_term_memory"


class MemoryManager:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=MEMORY_DB_PATH)
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        self.collection = self.client.get_or_create_collection(
            name=MEMORY_COLLECTION,
            embedding_function=self.embedding_fn
        )

    def store_finding(self, session_id: str, query: str, content: str):
        """Store a completed session's key finding as a long-term memory."""
        if not content:
            return
        memory_id = f"mem_{uuid.uuid4()}"
        self.collection.add(
            documents=[content],
            ids=[memory_id],
            metadatas=[{
                "session_id": session_id,
                "query": query,
                "created_at": datetime.now(timezone.utc).isoformat(),
            }]
        )

    def recall(self, query: str, n_results: int = 3) -> list[dict]:
        """Retrieve relevant past findings for a new query."""
        count = self.collection.count()
        if count == 0:
            return []

        results = self.collection.query(
            query_texts=[query],
            n_results=min(n_results, count)
        )

        memories = []
        docs = results.get("documents", [[]])[0]
        metas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        for doc, meta, distance in zip(docs, metas, distances):
            memories.append({
                "content": doc,
                "original_query": meta.get("query"),
                "created_at": meta.get("created_at"),
                "relevance_score": 1 - distance,
            })
        return memories