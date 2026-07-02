# Mini RAG Architecture

## Project Overview

Mini RAG is a lightweight, production-pattern Retrieval-Augmented Generation (RAG) system that demonstrates modular, maintainable patterns for document ingestion, semantic search, and LLM-powered question answering. It provides pluggable components for chunking documents, embedding text, indexing vectors, ranking results, and orchestrating complete end-to-end RAG workflows with clean separation of concerns across application, domain, and infrastructure layers.

## High Level Architecture

```
Application Layer
├── Ingestion
│   └── DocumentIngestionService
├── Indexing
│   └── Indexer
├── Retrieval
│   └── DefaultRetriever
└── RAG Services
    └── DefaultRagService

Domain Layer (Entities & Contracts)
├── Chunk
├── IndexedChunk
├── SearchResult
├── VectorSearchResult
├── SourceDocument
├── Prompt
└── Abstract Contracts
    ├── Chunker
    ├── Retriever
    ├── RagService
    ├── Reranker
    └── LLMClient

Infrastructure Layer
├── Embedding
│   ├── EmbeddingService (abstract)
│   └── SentenceTransformerEmbeddingService (impl)
├── Vector Index
│   ├── VectorStore (abstract)
│   └── FAISS
│       ├── FaissVectorIndex (impl)
│       └── Vector utilities
├── Repository
│   ├── ChunkRepository (abstract)
│   ├── InMemoryChunkRepository (impl)
│   └── SearchResultMapper (infra → domain)
└── LLM
    ├── LLMClient (abstract)
    └── FakeLLMClient (impl)

Utilities
├── Chunking Strategies
│   ├── WordChunker
│   ├── SlidingWindowSentenceChunker
│   └── FixedSizeChunker
├── Prompt Building
│   ├── PromptBuilder (abstract)
│   └── DefaultPromptBuilder (impl)
├── Re-ranking
│   ├── Reranker (abstract)
│   └── FakeReranker (impl)
├── Similarity
│   └── CosineSimilarity
└── Chunk Utils
    └── ChunkUtils (chunking helpers)

Tests & Experiments
├── Unit & Integration Tests
└── Playground Code
```

## Folder Structure

| Folder | Purpose | Status |
|--------|---------|--------|
| `application/` | Orchestrates workflows: ingestion, indexing, retrieval, and RAG services | ✅ Complete |
| `application/ingestion/` | Document ingestion pipeline | ✅ Complete |
| `application/indexing/` | Indexing pipeline orchestration | ✅ Complete |
| `application/retrieval/` | Retrieval orchestration | ✅ Complete |
| `application/services/` | RAG service implementations | ✅ Complete |
| `chunking/` | Document splitting strategies (word, sentence, fixed-size) | ✅ Complete |
| `domain/` | Core business entities and abstract contracts | ✅ Complete |
| `infrastructure/` | External implementations (embedding, vector store, repository, LLM) | ✅ Complete |
| `infrastructure/embedding/` | Embedding service implementations | ✅ Complete |
| `infrastructure/vector_index/` | Vector store implementations (FAISS) | ✅ Complete |
| `infrastructure/repository/` | Chunk repository and result mapping | ✅ Complete |
| `llm/` | LLM client abstraction and implementations | ✅ Complete |
| `prompting/` | Prompt building and template logic | ✅ Complete |
| `reranker/` | Result re-ranking strategies | ✅ Complete |
| `similarity/` | Similarity calculations (cosine, etc.) | ✅ Complete |
| `utils/` | Utility functions (math utilities) | ✅ Complete |
| `experiments/` | Playground code and prototypes | ✅ Complete |
| `tests/` | Test suites and demonstrations | ✅ Complete |
| `docs/` | Architecture, decisions, and roadmap documentation | ✅ Complete |

## Indexing Flow

```
SourceDocument
    ↓
DocumentIngestionService.ingest()
    ↓
Chunker.chunk()
    ↓
List[Chunk]
    ↓
Indexer.index()
    ├─→ EmbeddingService.embed()
    ├─→ VectorIndex.add()
    └─→ ChunkRepository.add()
```

**Reingest Support:** DocumentIngestionService supports `reingest()` to replace indexed documents by their ID.

## End-to-End RAG Flow

```
User Query
    ↓
DefaultRagService.ask()
    ├─→ Retriever.retrieve(query, top_k)
    │   ├─→ EmbeddingService.embed()
    │   ├─→ VectorIndex.search()
    │   ├─→ ChunkRepository.get(chunk_id)
    │   └─→ SearchResult (domain model)
    ├─→ PromptBuilder.build(query, List[SearchResult])
    │   └─→ Prompt (formatted with context)
    └─→ LLMClient.generate(Prompt)
        └─→ Generated Response
```

**Retrieval Details:**
- Vector Index finds candidates by semantic similarity
- ChunkRepository hydrates results with full chunk metadata
- Retriever returns domain `SearchResult` objects (infrastructure models stay isolated)
- PromptBuilder formats results into LLM-ready prompts

## Component Responsibilities

### Application Layer

**DocumentIngestionService**
- Accepts `SourceDocument` instances
- Coordinates chunking and indexing pipelines
- Supports document reingest (delete old, index new)
- Delegates to `Chunker` and `Indexer`

**Indexer**
- Receives `List[Chunk]` from chunker (domain model, not infrastructure)

**DefaultRagService**
- Orchestrates complete RAG pipeline
- Calls `Retriever` to get relevant chunks
- Constructs prompt via `PromptBuilder`
- Generates response via `LLMClient`
- Configurable `top_k` for retrieval (default: 5)

### Domain Layer (Contracts)

**Chunker (Abstract)**
- Splits `SourceDocument` into `List[Chunk]`
- Concrete implementations handle different strategies

**Retriever (Abstract)**
- Retrieves `List[SearchResult]` given query and top_k

**RagService (Abstract)**
- Public interface for RAG workflows
- Implements `ask(query) → str`

**PromptBuilder (Abstract)**
- ConstrFaissVectorIndex** (production-ready)
- [x] Vector normalization & utility functions

### Repository
- [x] **ChunkRepository** (abstract)
- [x] **InMemoryChunkRepository** (development/testing)
- [x] **SearchResultMapper** (infrastructure → domain
**Reranker (Abstract)**
- Re-ranks search results
- Accepts query, results, and top_k

### Infrastructure Layer

**EmbeddingService (Abstract)**
- `embed(text: str) → list[float]`: Single text embedding
- `embed_batch(texts: list[str]) → list[list[float]]`: Batch embeddings

**SentenceTransformerEmbeddingService (Impl)**
- Uses Sentence Transformers (`all-MiniLM-L6-v2`)
- Returns 384-dimensional embeddings
- Supports single and batch operations

**VectorStore (Abstract)**
- `add(indexed_chunk: IndexedChunk)`: Store vector + chunk
- `search(query_vector, top_k) → list[SearchResult]`: Semantic search
- `delete(chunk_id)`: Remove by chunk ID
- `delete_by_source_document(doc_id)`: Bulk delete by source

**FaissVectorIndex (Impl)**
- FAISS library wrapper
- IndexFlatIP for exact search
- L2 normalization on vectors
- Production-ready approximate search ready

**ChunkRepository (Abstract)**
- `add(chunk: Chunk)`: Store chunk metadata
- `get(chunk_id) → Chunk`: Retrieve by ID
- `delete(chunk_id)`: Remove by ID
- `delete_by_source_document(doc_id)`: Bulk operations

**InMemoryChunkRepository (Impl)**
- In-memory dictionary-based storage
- Supports source document-scoped deletion

**SearchResultMapper**
- Converts infrastructure-layer results to domain `SearchResult`
- Ensures infrastructure models don't leak to application layer

**LLMClient (Abstract)**
- `generate(prompt: Prompt) → str`: Generate response

**FakeLLMClient (Impl)**
- Returns formatted prompt for testing/demos
- Useful for development and validation

## - Searches `VectorIndex` for similar vectors
- Retrieves full chunk data from `ChunkRepository`
- Returns ordered `List[SearchResult]`

**DefaultRagService**
- Orchestrates complete RAG pipeline
- Calls `Retriever` to get relevant chunks
- Constructs prompt via `PromptBuilder`
- Generates response via `LLMClient`
- Configurable `top_k` for retrieval (default: 5)
Implemented Components (v1.0)

### Chunking Strategies
- [x] **WordChunker** — Split on word boundaries
- [x] **SlidingWindowSentenceChunker** — Overlapping sentence windows
- [x] **FixedSizeChunker** — Fixed character length chunks
- [x] **ChunkUtils** — Common chunking utilities

### Embedding
- [x] **EmbeddingService** (abstract)
- [x] **SentenceTransformerEmbeddingService** (384-dim, all-MiniLM-L6-v2)
- [x] Batch embedding support

### Vector Stores
- [x] **VectorStore** (abstract)
- [x] **InMemoryVectorStore** (development/testing)
- [x] **FaissVectorIndex** (production-ready)
- [x] Vector normalization & utility functions

### Repository
- [x] **ChunkRepository** (abstract)
- [x] **InMemoryChunkRepository** (development/testing)

### Retrieval
- [x] **Retriever** (abstract)
- [x] **DefaultRetriever** (vector + metadata lookup)

### Orchestration
- [x] **Indexer** — Coordinates embedding & storage
- [x] **DocumentIngestionService** — Full ingestion pipeline
- [x] **DefaultRagService** — Complete RAG workflow

### Prompting
- [x] **PromptBuilder** (abstract)
- [x] **DefaultPromptBuilder** (context + query formatting)

### LLM Integration
- [x] **LLMClient** (abstract)
- [x] **FakeLLMClient** (for testing/demos)

### Re-ranking
- [x] **Reranker** (abstract)
- [x] **FakeReranker** (passthrough, top-k filtering)

### Utilities
- [x] **CosineSimilarity** (vector similarity calculation)
- [x] **ChunkUtils** (chunk utilities)
- [x] **MathUtils** (mathematical utilities)

### Domain Models
- [x] **Chunk** — Indexed content unit
- [x] **IndexedChunk** — Chunk + embedding
- [x] **SourceDocument** — Input document
- [x] **SearchResult** — Retrieval result
- [x] **VectorSearchResult** — Raw vector search result
- [x] **Prompt** — LLM prompt object

### Integration & Testing
- [x] **Main app.py** — End-to-end example
- [x] **Test suites** — Core functionality tests
- [x] **Experiment modules** — FAISS playground & demo and search results
- Enables prompt template customization

**LLMClient (Abstract)**
- Generates response string from `Prompt`
- Abstracts LLM provider details

**Reranker (Abstract)**
- Re-ranks search results
- Accepts query, results, and top_k

### Infrastructure Layer

**EmbeddingService (Abstract)**
- `embed(text: str) → list[float]`: Single text embedding
- `embed_batch(texts: list[str]) → list[list[float]]`: Batch embeddings

**SentenceTransformerEmbeddingService (Impl)**
- Uses Sentence Transformers (`all-MiniLM-L6-v2`)
- Returns 384-dimensional embeddings
- Supports single and batch operations

**VectorStore (Abstract)**
- `add(indexed_chunk: IndexedChunk)`: Store vector + chunk
- `search(query_vector, top_k) → list[SearchResult]`: Semantic search
- `delete(chunk_id)`: Remove by chunk ID
- `delete_by_source_document(doc_id)`: Bulk delete by source

**InMemoryVectorStore (Impl)**
- In-memory dictionary-based storage
- Uses `CosineSimilarity` for ranking
- Supports filtering by source document

**FaissVectorIndex (Impl)**
- FAISS library wrapper
- IndexFlatIP for exact search
- L2 normalization on vectors
- Production-ready approximate search ready

**ChunkRepository (Abstract)**
- `add(chunk: Chunk)`: Store chunk metadata
- `get(chunk_id) → Chunk`: Retrieve by ID
- `delete(chunk_id)`: Remove by ID
- `delete_by_source_document(doc_id)`: Bulk operations

**InMemoryChunkRepository (Impl)**
- In-memory dictionary-based storage
- Supports source document-scoped deletion

**LLMClient (Abstract)**
- `generate(prompt: Prompt) → str`: Generate response

**FakeLLMClient (Impl)**
- Returns formatted prompt for testing/demos
- Useful for development and validation

## Current Components

- [x] WordChunker
- [x] SlidingWindowSentenceChunker
- [x] FixedSizeChunker
- [x] SentenceTransformerEmbeddingService
- [x] FaissVectorIndex
- [x] InMemoryVectorStore
- [x] ChunkRepository (In-Memory)
- [x] Indexer
- [x] Retriever
- [x] PromptBuilder
- [x] FakeLLMClient
- [x] RagService
- [x] SearchResultMapper
- [x] Cosine Similarity Utilities
