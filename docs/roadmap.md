# Mini RAG Roadmap

## Version 1.0 - Complete ✅

Mini RAG v1.0 is a fully functional RAG system with clean architecture, modular components, and production-grade patterns.

## Completed (v1.0)

### Chunking & Ingestion
- [x] Word-based chunking strategy
- [x] Sliding window sentence chunking
- [x] Fixed-size character chunking
- [x] ChunkUtils for shared chunking logic
- [x] DocumentIngestionService with reingest support
- [x] Chunk domain model with metadata support

### Embedding & Similarity
- [x] EmbeddingService abstraction
- [x] SentenceTransformerEmbeddingService (384-dim, all-MiniLM-L6-v2)
- [x] Single and batch embedding support
- [x] CosineSimilarity calculation
- [x] Vector normalization (L2)

### Vector Storage
- [x] VectorStore abstraction
- [x] InMemoryVectorStore for development/testing
- [x] FaissVectorIndex for production use
- [x] IndexFlatIP with cosine similarity
- [x] Vector indexing and search
- [x] Bulk delete by source document

### Repository & Metadata
- [x] ChunkRepository abstraction
- [x] InMemoryChunkRepository implementation
- [x] Chunk storage with metadata
- [x] IndexedChunk model
- [x] Source document tracking

### Retrieval & Search
- [x] Retriever abstraction
- [x] DefaultRetriever implementation
- [x] Vector similarity search
- [x] Chunk hydration from repository
- [x] SearchResult domain model
- [x] VectorSearchResult model
- [x] Search result ranking and filtering

### Orchestration & Workflow
- [x] Indexer class for embedding & storage
- [x] DefaultRagService for end-to-end RAG
- [x] RagService abstraction
- [x] Configurable top_k for retrieval
- [x] Clean workflow separation

### Prompting & LLM Integration
- [x] PromptBuilder abstraction
- [x] DefaultPromptBuilder implementation
- [x] Structured prompt formatting
- [x] Context + question templates
- [x] Prompt domain model
- [x] LLMClient abstraction
- [x] FakeLLMClient for testing/demos

### Re-ranking
- [x] Reranker abstraction
- [x] FakeReranker implementation (passthrough + top-k)
- [x] Ready for cross-encoder integration

### Domain & Contracts
- [x] Chunk domain model
- [x] SourceDocument model
- [x] SearchResult model
- [x] VectorSearchResult model
- [x] Prompt model
- [x] IndexedChunk model
- [x] All abstract contracts (Chunker, Retriever, LLMClient, etc.)

### Integration & Examples
- [x] End-to-end main.py example
- [x] Complete app.py demonstration
- [x] All components wired together
- [x] Working RAG pipeline from ingest to generate

### Testing & Experiments
- [x] FAISS playground (faiss_playground.py)
- [x] Vector store demo (vector_store_demo.py)
- [x] Cosine similarity demo (cosine-demo.py)
- [x] FAISS vector index tests
- [x] Unit test structure in place

### Documentation
- [x] architecture.md (complete with diagrams & responsibilities)
- [x] decisions.md (14 ADRs covering all major decisions)
- [x] roadmap.md (v1 completion status)
- [x] README.md (project overview & setup)

## In Progress

None — v1.0 is complete!

## Future Roadmap (v2.0+)

### Advanced Search Features
- [ ] Hybrid search (dense + sparse/BM25)
- [ ] Query expansion and reformulation
- [ ] Multi-vector retrieval
- [ ] Metadata filtering and SQL-like queries

### Production Vector Stores
- [ ] HNSW (Hierarchical Navigable Small World) integration
- [ ] Persistent FAISS index serialization
- [ ] Pinecone integration
- [ ] ChromaDB integration
- [ ] Weaviate integration
- [ ] Milvus integration

### LLM Providers
- [ ] OpenAI integration (GPT-3.5, GPT-4)
- [ ] Anthropic Claude integration
- [ ] Hugging Face inference API
- [ ] Local LLM support (Ollama, LLaMA)
- [ ] Azure OpenAI integration

### Advanced Re-ranking
- [ ] Cross-encoder re-ranking
- [ ] Semantic re-ranking
- [ ] Diversity-aware re-ranking
- [ ] Query-aware re-ranking

### Semantic Chunking
- [ ] Semantic similarity-based chunking
- [ ] Hierarchical chunking (chapters → sections → paragraphs)
- [ ] Table and code-aware chunking
- [ ] Multi-modal chunking (text + images)

### Evaluation & Observability
- [ ] Retrieval evaluation framework (recall, NDCG, MRR)
- [ ] Generation quality metrics (BLEU, ROUGE)
- [ ] Logging and tracing infrastructure
- [ ] Metrics collection (latency, cost, quality)
- [ ] Debugging tools for retrieval chains

### Performance & Caching
- [ ] Query result caching
- [ ] Embedding cache
- [ ] LLM response cache
- [ ] TTL-based cache invalidation

### Persistence & Storage
- [ ] PostgreSQL for chunk metadata
- [ ] S3 for chunk content
- [ ] Distributed indexing
- [ ] Backup and recovery mechanisms

### API & Deployment
- [ ] FastAPI web server
- [ ] REST API endpoints
- [ ] WebSocket support for streaming
- [ ] GraphQL API option
- [ ] Docker containerization
- [ ] Kubernetes deployment manifests

### Advanced Features
- [ ] Multi-document QA chains
- [ ] Conversational RAG with memory
- [ ] Contextual follow-up questions
- [ ] Citation and source attribution
- [ ] Explainability for retrieval decisions
- [ ] A/B testing framework

### Data Management
- [ ] Document versioning
- [ ] Incremental indexing
- [ ] Document lifecycle management
- [ ] Bulk document operations
- [ ] Data lineage tracking
