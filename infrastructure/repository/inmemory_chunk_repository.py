from domain.indexed_chunk import IndexedChunk
from infrastructure.repository.chunk_repository import ChunkRepository


class InMemoryChunkRepository(ChunkRepository):
    def __init__(self):
        self._chunks_by_vector_id: dict[int, IndexedChunk] = {}
        self._vector_ids_by_document_id: dict[str, set[int]] = {}


    def save(self, vector_id: int, indexed_chunk: IndexedChunk):

        self._chunks_by_vector_id[vector_id] = indexed_chunk
        document_id = indexed_chunk.chunk.source_document_id

        if document_id not in self._vector_ids_by_document_id:
            self._vector_ids_by_document_id[document_id] = set()

        self._vector_ids_by_document_id[document_id].add(vector_id)



    def find_by_vector_id(self, vector_id: int) -> IndexedChunk:
        return self._chunks_by_vector_id.get(vector_id)
    

    
    def delete_by_vector_id(self, vector_id: int) -> None:
        indexed_chunk = self._chunks_by_vector_id.pop(vector_id, None)

        if indexed_chunk is None:
            return
        
        document_id = indexed_chunk.source_document_id

        vector_ids = self._vector_ids_by_document_id.get(document_id)

        if vector_ids is None:
            return
        
        vector_ids.discard(vector_id)

        if len(vector_ids) == 0:
            self._vector_ids_by_document_id.pop(document_id, None)


    
    def delete_by_document_id(self, document_id: str) -> None:
        vector_ids = self._vector_ids_by_document_id.get(document_id)

        if vector_ids is None:
            return
        
        for vector_id in vector_ids:
            self._chunks_by_vector_id.pop(vector_id, None)
        
        self._vector_ids_by_document_id.pop(document_id, None)


    
