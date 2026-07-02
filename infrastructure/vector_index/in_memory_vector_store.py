from domain.indexed_chunk import IndexedChunk
from domain.search_result import SearchResult
from similarity.cosine_similarity import CosineSimilarity
from infrastructure.vector_index import VectorStore


class InMemoryVectorStore(VectorStore):
    def __init__(self):
        self.chunks : dict[str, IndexedChunk] = {}

    def upsert(self, indexed_chunk: IndexedChunk):
        self.chunks[indexed_chunk.chunk.chunk_id] = indexed_chunk


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
    
    def delete_by_source_document(self, source_document_id: str):
        chunks_to_delete = [chunk_id for chunk_id, indexed_chunk in self.chunks.items() if indexed_chunk.chunk.source_document_id == source_document_id]
        for chunk_id in chunks_to_delete:
            del self.chunks[chunk_id]