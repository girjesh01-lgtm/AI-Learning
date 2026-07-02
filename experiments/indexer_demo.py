from application.indexing.indexer import Indexer
from domain.chunk import Chunk
from infrastructure.embedding.sentence_transformer_embedding_service import SentenceTransformerEmbeddingService
from infrastructure.repository.inmemory_chunk_repository import InMemoryChunkRepository
from infrastructure.vector_index.faiss.faiss_vector_index import FaissVectorIndex


embedding_service = SentenceTransformerEmbeddingService()

vector_index = FaissVectorIndex(
    dimension=384
)

repository = InMemoryChunkRepository()

indexer = Indexer(
    embedding_service,
    vector_index,
    repository
)



chunks = [

    Chunk(
        chunk_id="1",
        source_document_id="doc1",
        chunk_index=0,
        text="Java is a programming language.",
        metadata={}
    ),

    Chunk(
        chunk_id="2",
        source_document_id="doc1",
        chunk_index=1,
        text="Spring Boot is used for backend development.",
        metadata={}
    )

]

indexed_chunks = indexer.index(
    chunks
)
print(vector_index.index.ntotal)

#print(indexed_chunks)

print(
    repository.find_by_vector_id(0)
)

print(
    repository.find_by_vector_id(1)
)