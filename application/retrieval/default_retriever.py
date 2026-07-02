from application.retrieval.search_result_mapper import SearchResultMapper
from domain.search_result import SearchResult
from domain.vector_search_result import VectorSearchResult
from infrastructure.embedding.embedding_service import EmbeddingService 
from application.retrieval.retriever import Retriever 
from infrastructure.repository.chunk_repository import ChunkRepository 
from infrastructure.vector_index.faiss.vector_index import VectorIndex 

class DefaultRetriever(Retriever): 
    def __init__(self, 
                 embedding_service: EmbeddingService, 
                 vector_index: VectorIndex, 
                 chunk_repository: ChunkRepository
                 ): 
            self.embedding_service = embedding_service
            self.vector_index = vector_index
            self.chunk_repository = chunk_repository


    def retrieve(self, query_text: str, top_k: int):

        query_vector = self.embedding_service.embed(query_text)

        vector_results = self.vector_index.search(query_vector, top_k)
        
        indexed_chunks = []

        for vector_result in vector_results:
            
            indexed_chunk = self.chunk_repository.find_by_vector_id(vector_result.vector_id)

            if indexed_chunk is None:
                 continue
            
            indexed_chunks.append(indexed_chunk)

        return self._to_search_results(vector_results)
    

    def _to_search_results(self, vector_results: list[VectorSearchResult]) -> list[SearchResult]:
        search_results = []

        for vector_result in vector_results:
            
            indexed_chunk = self.chunk_repository.find_by_vector_id(vector_result.vector_id)

            if indexed_chunk is None:
                 continue
            
            search_results.append(SearchResultMapper.to_search_result(indexed_chunk=indexed_chunk, vector_search_result=vector_result))

        return search_results