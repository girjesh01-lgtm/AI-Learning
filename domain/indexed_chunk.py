from dataclasses import dataclass

from domain.chunk import Chunk

@dataclass(frozen=True)
class IndexedChunk:
    chunk:Chunk
    embedding: list[float]