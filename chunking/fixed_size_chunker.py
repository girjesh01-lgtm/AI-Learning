from chunking.chunker import Chunker
from models.chunk import Chunk
from models.source_document import SourceDocument


class FixedSizeChunker(Chunker):
    def __init__(self, chunk_size: int = 500):
        self.chunk_size = chunk_size

    def chunk(self, source_document: SourceDocument) -> list[Chunk]:
        chunks = []
        text = source_document.text
        start = 0
        chunk_index = 0

        while start < len(text):
            end = start + self.chunk_size
            chunk_text = text[start:end]
            chunks.append(Chunk(
                chunk_id = f"{source_document.document_id}_chunk_{chunk_index}",
                source_document_id = source_document.document_id,
                chunk_index = chunk_index,
                text = chunk_text,
                metadata = source_document.metadata.copy()
            ))

            start = end
            chunk_index += 1
        return chunks