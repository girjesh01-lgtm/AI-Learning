from dataclasses import dataclass

from models.indexed_chunk import IndexedChunk

@dataclass
class SearchResult:
    indexed_chunk: IndexedChunk
    similarity_score: float