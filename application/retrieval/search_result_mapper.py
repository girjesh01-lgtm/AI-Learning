from domain import chunk
from domain.indexed_chunk import IndexedChunk
from domain.search_result import SearchResult
from domain.vector_search_result import VectorSearchResult


class SearchResultMapper:
    
    @staticmethod
    def to_search_result(
        indexed_chunk: IndexedChunk, 
        vector_search_result: VectorSearchResult
        ) -> SearchResult:
        
        return SearchResult(
            chunk=indexed_chunk.chunk,
            similarity_score=vector_search_result.similarity_score
        )