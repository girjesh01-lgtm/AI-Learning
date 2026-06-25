from embedding.embedding_service import EmbeddingService
from retrieval.retriever import Retriever
from vectordb.in_memory_vector_store import VectorStore

class DefaultRetriever(Retriever):

    def __init__(self, vector_store: VectorStore, embedding_service: EmbeddingService):
        self.vector_store = vector_store
        self.embedding_service = embedding_service

    def retrieve(self, query_text: str, top_k: int):
        query_vector = self.embedding_service.embed(query_text)
        return self.vector_store.search(query_vector=query_vector, top_k=top_k)
    