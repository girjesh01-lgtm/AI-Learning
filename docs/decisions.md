# Architecture Decision Records

## ADR-001: Chunking Responsibility

**Status:** Accepted

**Decision:** Document chunking is the responsibility of `DocumentIngestionService` and specialized `Chunker` implementations, not the `Indexer`.

**Reason:** Chunking is inherently tied to document format and ingestion strategy. Separating it allows multiple chunking strategies to coexist without duplicating indexing logic. The `Indexer` should assume chunks already exist.

**Consequences:** 
- Simpler `Indexer` interface
- `DocumentIngestionService` becomes more complex but handles cohesive ingestion concerns
- Easy to add new chunking strategies
- Supports reingest operations (delete old, index new)

---

## ADR-002: Indexer Input Contract

**Status:** Accepted

**Decision:** `Indexer` receives `List[Chunk]` and is responsible only for embedding and storing them.

**Reason:** Provides a clear, testable contract. The indexer doesn't need to know about document parsing or chunking strategy.

**Consequences:**
- Indexer is lightweight and focused
- All integration concerns live in `DocumentIngestionService`
- Easy to test indexer in isolation

---

## ADR-003: VectorIndex Abstraction

**Status:** Accepted

**Decision:** `VectorIndex` only understands vector embeddings and vector IDs. It does not store or manage chunk metadata.

**Reason:** Keeps the vector store decoupled from domain logic and metadata concerns. Multiple vector stores (FAISS, Pinecone, etc.) can implement the same interface.

**Consequences:**
- `VectorIndex` remains simple and database-agnostic
- Metadata is the responsibility of `ChunkRepository`
- Easier to swap vector store implementations

---

## ADR-004: Metadata Storage

**Status:** Accepted

**Decision:** Chunk metadata (content, source, created_at, etc.) is stored in `ChunkRepository`, not in `VectorIndex`.

**Reason:** Metadata schemas vary by use case. Keeping it separate allows independent scaling and flexibility.

**Consequences:**
- Retrieval requires two lookups: one in `VectorIndex` (by vector similarity), one in `ChunkRepository` (by chunk ID)
- Clear separation of concerns
- Enables independent optimization of each store

---

## ADR-005: FAISS as Vector Store

**Status:** Accepted

**Decision:** Use FAISS for in-memory vector indexing in development and proof-of-concept deployments.

**Reason:** FAISS is mature, fast, and suitable for prototyping. It provides exact and approximate search algorithms without external dependencies.

**Consequences:**
- Vectors are stored in-memory; not persistent by default
- Suitable for demonstrations but not production at scale
- Swappable with persistent vector databases (Pinecone, Chroma, etc.)
- IndexFlatIP used for exact search with cosine similarity

---

## ADR-006: Search Result Mapping

**Status:** Accepted

**Decision:** Use `SearchResultMapper` to convert infrastructure-layer search results into domain `SearchResult` objects.

**Reason:** Maintains the boundary between infrastructure concerns and domain logic. Infrastructure models are internal; domain models are the public API.

**Consequences:**
- Additional mapping layer adds minimal overhead
- Domain layer is independent of vector store implementation details
- Type safety across layer boundaries

---

## ADR-007: Retrieval Pipeline

**Status:** Accepted

**Decision:** Retrieval uses `VectorIndex` first (semantic search), followed by `ChunkRepository` lookup (metadata retrieval).

**Reason:** Efficient two-stage lookup: search by similarity first, hydrate with metadata second.

**Consequences:**
- Retriever depends on both `VectorIndex` and `ChunkRepository`
- Enables filtering and re-ranking post-search
- Retrieval is stateless and testable

---

## ADR-008: Application Layer Orchestration

**Status:** Accepted

**Decision:** Application layer (`RagService`, ingestion services, retrieval services) orchestrates workflows; infrastructure implements building blocks.

**Reason:** Keeps workflows explicit and testable. Infrastructure is substitutable.

**Consequences:**
- Application layer is stateful; infrastructure is stateless
- Easy to mock infrastructure for testing
- Clear workflow logic visible in application code

---

## ADR-009: Retriever Returns Domain Models

**Status:** Accepted

**Decision:** `Retriever` returns `SearchResult` (domain model) instead of infrastructure models like `IndexedChunk`.

**Reason:** Keep infrastructure models (FAISS details, raw embeddings) inside the infrastructure layer. The application and retrieval layers work only with domain models.

**Consequences:**
- Infrastructure implementations remain hidden from application code
- SearchResultMapper handles infrastructure → domain conversion
- Easy to swap vector stores without affecting application layer
- Type safety across layer boundaries
- Clear separation between infrastructure concerns and business logic

---

## ADR-010: Fake Implementations for Testing

**Status:** Accepted

**Decision:** Provide `FakeLLMClient`, `FakeReranker`, and in-memory implementations for development and testing.

**Reason:** Reduces external dependencies during development. Enables fast iteration without costly API calls.

**Consequences:**
- Developers can test end-to-end flows offline
- Production implementations are swapped in at deployment
- Clear path from dev to prod (interface-based)

---

## ADR-011: Multiple Chunking Strategies

**Status:** Accepted

**Decision:** Support `WordChunker`, `SlidingWindowSentenceChunker`, and `FixedSizeChunker` as initial strategies.

**Reason:** Different use cases require different chunking approaches. Pluggable strategies allow optimization per domain.

**Consequences:**
- Chunker interface is simple and composable
- Easy to add new strategies (e.g., semantic chunking, hierarchical)
- ChunkUtils provides shared chunking logic

---

## ADR-012: Sentence Transformers for Embeddings

**Status:** Accepted

**Decision:** Use Sentence Transformers (`all-MiniLM-L6-v2`) for embedding service (384 dimensions).

**Reason:** Lightweight, fast, and pre-trained for semantic similarity. No external API required.

**Consequences:**
- Offline embedding capability
- Deterministic, reproducible embeddings
- Supports batch operations for efficiency
- Easy to swap for other models (BERT, DPR, etc.)

---

## ADR-013: DefaultPromptBuilder Template

**Status:** Accepted

**Decision:** Prompt builder constructs structured prompts with system instruction, context chunks, and question.

**Reason:** Consistent prompt format across all LLM calls. Easy to customize prompts without changing workflow.

**Consequences:**
- Prompts are deterministic and debuggable
- Easy to test prompt quality
- Can iterate on prompt templates independently

---

## ADR-014: Re-ranking as Optional Pipeline Stage

**Status:** Accepted

**Decision:** Re-ranking is an optional post-retrieval step via `Reranker` interface.

**Reason:** Not all RAG systems need re-ranking. Pluggable interface allows conditional use.

**Consequences:**
- FakeReranker provides passthrough + top-k filtering for testing
- Production rerankers (cross-encoders, etc.) can be integrated
- Retrieval quality can be improved without changing core pipeline
