from infrastructure.vector_index.faiss.faiss_vector_index import FaissVectorIndex

index = FaissVectorIndex(4)

index.add([1, 0, 0, 0])
index.add([0, 1, 0, 0])
index.add([0, 0, 1, 0])

results = index.search(
    [1, 0, 0, 0],
    top_k=3
)

for result in results:
    print(result)