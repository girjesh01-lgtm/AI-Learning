from application.indexing.indexer import Indexer
from application.ingestion.document_ingestion_service import DocumentIngestionService
from application.retrieval.default_retriever import DefaultRetriever
from application.services.default_rag_service import DefaultRagService
from chunking.sliding_window_sentence_chunker import SlidingWindowSentenceChunker
from domain.source_document import SourceDocument
from infrastructure.embedding.sentence_transformer_embedding_service import SentenceTransformerEmbeddingService
from infrastructure.repository.inmemory_chunk_repository import InMemoryChunkRepository
from infrastructure.vector_index.faiss.faiss_vector_index import FaissVectorIndex
from llm.fake_llm_client import FakeLLMClient
from prompting.default_prompt_builder import DefaultPromptBuilder


embedding_service = SentenceTransformerEmbeddingService()

vector_index = FaissVectorIndex(384)

chunk_repository = InMemoryChunkRepository()

chunker = SlidingWindowSentenceChunker()

indexer = Indexer(
    embedding_service,
    vector_index,
    chunk_repository
)

ingestion_service = DocumentIngestionService(
    chunker,
    indexer
)

retriever = DefaultRetriever(
    embedding_service,
    vector_index,
    chunk_repository
)

prompt_builder = DefaultPromptBuilder()

llm = FakeLLMClient()

rag_service = DefaultRagService(
    retriever,
    prompt_builder,
    llm
)


document = SourceDocument(
    document_id="doc1",
    text="""
Java is an object-oriented programming language.

Spring Boot simplifies Java backend development.

Dependency Injection is one of Spring Framework's core features.

Spring Boot provides auto-configuration.

Python is commonly used for Machine Learning.

FAISS is a vector similarity search library developed by Meta.
""",
    metadata={}
)

ingestion_service.ingest(document)



response = rag_service.ask(
   "What is Kubernetes?"
)

print(response)