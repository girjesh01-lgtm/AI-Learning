from dataclasses import dataclass

from models.chunk import Chunk

@dataclass(frozen=True)
class IndexedChunk:
    chunk:Chunk
    embedding: list[float]