import faiss
import numpy as np

dimensions = 4

index = faiss.IndexFlatIP(dimensions)

#print(index)

vectors = np.array([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0]
], dtype=np.float32)

index.add(vectors)

#print(index.ntotal)

query = np.array([
    [0.0, 1.0, 0.0, 0.0]
], dtype=np.float32)

distances, indices = index.search(query, 2)

print("Distances:", distances)
print("Indices:", indices)