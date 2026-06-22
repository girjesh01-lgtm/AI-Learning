from chunking.chunker import Chunker
from models.chunk import Chunk
from models.source_document import SourceDocument


class WordChunker(Chunker):
    def __init__(self, chunk_size: int):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")
        self.chunk_size = chunk_size

    def chunk(self, source_document: SourceDocument) -> list[Chunk]:
        words = source_document.text.split()
        chunks = []

        for i in range(0, len(words), self.chunk_size):
            chunk_words = words[i : i + self.chunk_size]
            chunk_text = " ".join(chunk_words)
            chunk_index = i // self.chunk_size
            chunks.append(
                Chunk(
                    chunk_id=f"{source_document.document_id}:{chunk_index}",
                    source_document_id=source_document.document_id,
                    chunk_index=chunk_index,
                    text=chunk_text,
                    metadata=source_document.metadata.copy(),
                )
            )

        return chunks