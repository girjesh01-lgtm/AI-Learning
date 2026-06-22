import re

from chunking.chunk_utils import ChunkUtils
from chunking.chunker import Chunker
from models.chunk import Chunk
from models.source_document import SourceDocument


class SlidingWindowSentenceChunker(Chunker):
    def __init__(self, chunk_size: int = 2, overlap_size: int = 1):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")
        
        if overlap_size < 0:
            raise ValueError("overlap_size must be non-negative")
        
        if self.overlap_size >= self.chunk_size:
            raise ValueError("overlap_size must be less than chunk_size")
        
        self.chunk_size = chunk_size
        self.overlap_size = overlap_size

    def chunk(self, source_document: SourceDocument) -> list[Chunk]:
        text = source_document.text or ""
        sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text.strip()) if s.strip()]
        chunks = []

        if not sentences:
            return chunks

        if len(sentences) <= self.chunk_size:
            joined = " ".join(sentences)
            chunks.append(ChunkUtils.create_chunk(source_document, 0, joined))
            return chunks

        step = self.chunk_size - self.overlap_size
        for i in range(0, len(sentences), step):
            window = sentences[i : i + self.chunk_size]
            chunk_text = " ".join(window)
            if len(window) < self.overlap_size:
                break
            chunks.append(ChunkUtils.create_chunk(source_document, i, chunk_text))

        return chunks