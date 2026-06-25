from chunking.sliding_window_sentence_chunker import SlidingWindowSentenceChunker
from embedding.sentence_transformer_embedding_service import (
    SentenceTransformerEmbeddingService
)

from indexing.indexer import Indexer
from ingestion.document_ingestion_service import DocumentIngestionService
from models.source_document import SourceDocument
from retrieval.default_retriever import DefaultRetriever
from vectordb.in_memory_vector_store import InMemoryVectorStore, VectorStore



embedding_service = SentenceTransformerEmbeddingService()
vector_store = InMemoryVectorStore()

#chunker = FixedSizeChunker(chunk_size=100)
#chunker = WordChunker(chunk_size=10)
chunker = SlidingWindowSentenceChunker(chunk_size=2, overlap_size=1)

indexer = Indexer(vector_store=vector_store, embedding_service=embedding_service)

retriever = DefaultRetriever(vector_store=vector_store, embedding_service=embedding_service)

document = SourceDocument(
    document_id="employee_handbook",
    text="""Employees are entitled to 15 casual leaves every year. Medical insurance is available for all employees. The notice period is 60 days. Office timings are 9 AM to 6 PM.""",)

ingester = DocumentIngestionService(chunker=chunker, indexer=indexer)
chunks = ingester.ingest(document)
print("========== CHUNKS ==========")
for chunk in chunks:
    print(chunk.chunk_id)
    print(chunk.text)
    print(chunk.metadata)
    print()

indexer.index(chunks)

print("========== QUERY ==========")

results = retriever.retrieve(
    query_text="How many casual leaves do employees get?",
    top_k=2,
)

for result in results:

    print("--------------------------------")

    print(
        "Score:",
        result.similarity_score,
    )

    print(
        "Chunk ID:",
        result.indexed_chunk.chunk.chunk_id,
    )

    print(
        "Text:",
        result.indexed_chunk.chunk.text,
    )