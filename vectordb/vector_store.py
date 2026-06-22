from models.indexed_chunk import IndexedChunk
from models.search_result import SearchResult
from similarity.cosine_similarity import CosineSimilarity


class VectorStore:
    def __init__(self):
        self.chunks : dict[str, IndexedChunk] = {}

    def upsert(self, indexed_chunk: IndexedChunk):
        self.chunks[indexed_chunk.chunk.chunk_id] = indexed_chunk

    def get(self, chunk_id: str):
        return self.chunks.get(chunk_id)

    def delete(self, chunk_id: str):
        del self.chunks[chunk_id]

    def search(self, query_vector, top_k):

        results = []

        for chunk in self.chunks.values():
            similarity_score = CosineSimilarity.calculate(query_vector, chunk.embedding)
            results.append(SearchResult(indexed_chunk=chunk, similarity_score=similarity_score))

        results.sort(
            key=lambda item: item.similarity_score,
            reverse=True
        )

        return results[:top_k]