from abc import ABC, abstractmethod

from domain.search_result import SearchResult


class Reranker(ABC):

    @abstractmethod
    def rerank(
        self, 
        query: str, 
        search_results: list[SearchResult], 
        top_k: int
    ) -> list[SearchResult]:
        pass