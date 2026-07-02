from domain.search_result import SearchResult
from reranker.reranker import Reranker


class FakeReranker(Reranker):

    def rerank(self, query: str, search_results: list[SearchResult], top_k: int) -> list[SearchResult]:
        return search_results[:top_k]