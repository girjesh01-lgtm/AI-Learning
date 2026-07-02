from application.indexing.indexer import Indexer
from application.retrieval.default_retriever import DefaultRetriever
from chunking.sliding_window_sentence_chunker import SlidingWindowSentenceChunker
from domain.source_document import SourceDocument
from infrastructure.embedding.sentence_transformer_embedding_service import SentenceTransformerEmbeddingService
from infrastructure.repository.inmemory_chunk_repository import InMemoryChunkRepository
from infrastructure.vector_index.faiss.faiss_vector_index import FaissVectorIndex
from prompting.default_prompt_builder import DefaultPromptBuilder



embedding_service = SentenceTransformerEmbeddingService()
vector_index = FaissVectorIndex(dimension=384)
chunk_repository = InMemoryChunkRepository()

indexer = Indexer(
    embedding_service,
    vector_index,
    chunk_repository
)



retriever = DefaultRetriever(
    embedding_service=embedding_service,
    vector_index=vector_index,
    chunk_repository=chunk_repository
)

prompt_builder = DefaultPromptBuilder()

document = SourceDocument(
    document_id="java_notes",
    text="""
Java is an object oriented programming language.

Spring Boot is built on top of Spring Framework.

Python is widely used in AI.
""",
    metadata={}
)

chunker = SlidingWindowSentenceChunker()

chunks = chunker.chunk(document)
# Index the document
indexer.index(chunks)

print("Retrieving results for query: 'What is Java?'")

results = retriever.retrieve(
    "What is Java?",
    top_k=2
)


prompt = prompt_builder.build(
    "What is Java?",
    results
)

print(prompt.text)