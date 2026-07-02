from infrastructure.embedding.embedding_service import EmbeddingService
from domain.chunk import Chunk
from domain.indexed_chunk import IndexedChunk
from infrastructure.repository import chunk_repository
from infrastructure.repository.chunk_repository import ChunkRepository
from infrastructure.vector_index.faiss.vector_index import VectorIndex


class Indexer:

    def __init__(self, embedding_service: EmbeddingService, vector_index: VectorIndex, chunk_repository: ChunkRepository):
        self.embedding_service = embedding_service
        self.vector_index = vector_index
        self.chunk_repository = chunk_repository




    def index(self, chunks: list[Chunk]) -> list[IndexedChunk]:

        indexed_chunks = []

        created_vector_ids = []

        try:

            for chunk in chunks:

                embedding = self.embedding_service.embed(chunk.text)

                vector_id = self.vector_index.add(embedding)
                
                indexed_chunk = IndexedChunk(chunk=chunk, embedding=embedding)

                self.chunk_repository.save(vector_id, indexed_chunk)

                indexed_chunks.append(indexed_chunk)

                created_vector_ids.append(vector_id)


            return indexed_chunks

        except Exception:
           
           self._rollback(created_vector_ids)
           
           raise



    def _rollback(self, vector_ids: list[int]) -> None:
        for vector_id in vector_ids:
            try:
                self.vector_index.delete(vector_id)
            except Exception:
                pass
            
            self.chunk_repository.delete_by_vector_id(vector_id)