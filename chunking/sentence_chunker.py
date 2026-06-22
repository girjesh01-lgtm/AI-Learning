import re

from chunking.chunker import Chunker
from models.chunk import Chunk
from models.source_document import SourceDocument


class SentenceChunker(Chunker):
    def __init__(self, chunk_size: int = 2):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")
        self.chunk_size = chunk_size

    def chunk(self, source_document: SourceDocument) -> list[Chunk]:
        text = source_document.text or ""
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text.strip()) if s.strip()]
        chunks = []

        if not sentences:
            return chunks

        if len(sentences) <= self.chunk_size:
            joined = " ".join(sentences)
            chunks.append(
                Chunk(
                    chunk_id=f"{source_document.document_id}_chunk_0",
                    source_document_id=source_document.document_id,
                    chunk_index=0,
                    text=joined,
                    metadata=source_document.metadata.copy(),
                )
            )
            return chunks

        for i in range(len(sentences) - self.chunk_size + 1):
            window = sentences[i : i + self.chunk_size]
            chunk_text = " ".join(window)
            chunks.append(
                Chunk(
                    chunk_id=f"{source_document.document_id}_chunk_{i}",
                    source_document_id=source_document.document_id,
                    chunk_index=i,
                    text=chunk_text,
                    metadata=source_document.metadata.copy(),
                )
            )

        return chunks