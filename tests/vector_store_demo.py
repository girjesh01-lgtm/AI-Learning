from infrastructure.vector_index.faiss.faiss_vector_index import FaissVectorStore

store = FaissVectorStore(
    embedding_dimension=384
)

print(store.index)