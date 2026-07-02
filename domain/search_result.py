from dataclasses import dataclass

from domain.chunk import Chunk

@dataclass
class SearchResult:
    chunk: Chunk
    similarity_score: float