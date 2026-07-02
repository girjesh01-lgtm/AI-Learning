from domain.indexed_chunk import IndexedChunk


class ChunkRepository:
    def save(self, vector_id: int, indexed_chunk: IndexedChunk):
        # Save the indexed chunk to the database or any other storage
        pass


    def find_by_vector_id(self, vector_id: int) -> IndexedChunk:
        # Retrieve the indexed chunk from the database or any other storage
        pass

    def delete_by_vector_id(self, vector_id: int) -> None:
        pass

    def delete_by_document_id(self, document_id: str) -> None:
        # Delete the indexed chunk from the database or any other storage
        pass

    def exists(self, vector_id: int) -> bool:
        # Check if the indexed chunk exists in the database or any other storage
        pass