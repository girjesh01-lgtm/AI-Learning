from embedding.embedding_service import EmbeddingService
from models.chunk import Chunk
from models.indexed_chunk import IndexedChunk
from vectordb.in_memory_vector_store import VectorStore


class Indexer:
    def __init__(self, vector_store: VectorStore, embedding_service: EmbeddingService):
        self.vector_store = vector_store
        self.embedding_service = embedding_service


    def index(self, chunks: list[Chunk]):
        for chunk in chunks:
            embedding = self.embedding_service.embed(chunk.text)
            indexed_chunk = IndexedChunk(chunk=chunk, embedding=embedding)
            self.vector_store.upsert(indexed_chunk)

