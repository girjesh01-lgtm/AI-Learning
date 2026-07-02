from domain.chunk import Chunk
from domain.source_document import SourceDocument


class ChunkUtils:
    @staticmethod    
    def create_chunk(source_document: SourceDocument, chunk_index: int, text: str) -> Chunk:
        
        return Chunk(
            chunk_id=f"{source_document.document_id}:{chunk_index}",
            source_document_id=source_document.document_id,
            chunk_index=chunk_index,
            text=text,
            metadata=source_document.metadata.copy()
        )