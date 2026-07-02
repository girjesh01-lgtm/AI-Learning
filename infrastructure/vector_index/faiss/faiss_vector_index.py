import faiss
import numpy as np

from domain import VectorSearchResult


class FaissVectorIndex:

    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatIP(dimension)

    def add(self, vector: np.ndarray) -> int :
        vector_id = self.index.ntotal
        embedding = self._to_numpy_vector(vector)
        self.index.add(embedding)
        return vector_id

    def search(self, query_embedding: np.ndarray, top_k: int) -> list[VectorSearchResult]:
        query = self._to_numpy_vector(query_embedding)
        scores, ids = self.index.search(query, top_k)

        result = []

        for vector_id, score in zip(ids[0], scores[0]):
            if vector_id == -1:
                continue

            result.append(
                VectorSearchResult(
                    vector_id=int(vector_id),
                    similarity_score=float(score)
                )
            )

        return result


    def delete(self, vector_id: int):
        raise NotImplementedError("Delete will be implemented after we integrate IDMap.")

    def _to_numpy_vector(self, embedding:list[float]) -> np.ndarray:
        if len(embedding) != self.dimension:
            raise ValueError(
            f"Expected embedding dimension {self.dimension}, "
            f"but got {len(embedding)}"
        )

        vector = np.array([embedding], dtype=np.float32)

        faiss.normalize_L2(vector)

        return vector