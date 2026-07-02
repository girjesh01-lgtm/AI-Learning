from abc import ABC, abstractmethod

import numpy as np

from domain.vector_search_result import VectorSearchResult


class VectorIndex(ABC):
    @abstractmethod
    def add(self, vector: np.ndarray) -> int:
        pass

    @abstractmethod
    def search(self, query_embedding: np.ndarray, top_k: int) -> list[VectorSearchResult]:
        pass

    @abstractmethod
    def delete(self, vector_id: int):
        pass