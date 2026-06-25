from abc import ABC, abstractmethod

from models.indexed_chunk import IndexedChunk


class VectorStore(ABC):
    
    @abstractmethod
    def upsert(self, indexed_chunk: IndexedChunk):
        pass

    @abstractmethod
    def search(self, query_vector: list[float], top_k: int) -> list[IndexedChunk]:
        pass

    @abstractmethod
    def delete(self, chunk_id: str):
        pass
    
    @abstractmethod
    def delete_by_source_document(self, source_document_id: str):
        pass