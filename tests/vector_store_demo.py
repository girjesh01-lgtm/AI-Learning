from embedding.sentence_transformer_embedding_service import SentenceTransformerEmbeddingService
from retrieval.default_retriever import DefaultRetriever
from vectordb.document import Document
from vectordb.in_memory_vector_store import VectorStore

store = VectorStore()
embedding_service = SentenceTransformerEmbeddingService()

doc1_text = "Java is an object oriented programming language."
doc1 = Document(id="doc1", text=doc1_text, embedding=embedding_service.embed(doc1_text))

doc2_text = "Spring Boot simplifies enterprise development."
doc2 = Document(id="doc2", text=doc2_text, embedding=embedding_service.embed(doc2_text))

doc3_text = "Python is widely used in AI."
doc3 = Document(id="doc3", text=doc3_text, embedding=embedding_service.embed(doc3_text))

store.store(doc1)
store.store(doc2)
store.store(doc3)

retriever = DefaultRetriever(store, embedding_service)

#query_vector = [0.11, 0.31, 0.81]
query_text = "What is Java?"
top_k = 2

results = retriever.retrieve(query_text, top_k)

for result in results:
    print("----------------------------------------------")
    print(result.document.id)
    print(result.document.text)
    print(result.similarity_score)
