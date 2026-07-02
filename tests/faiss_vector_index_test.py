from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from infrastructure.vector_index.faiss.faiss_vector_index import FaissVectorIndex



index = FaissVectorIndex(4)

index.add([1,0,0,0])

index.add([0,1,0,0])

index.add([0,0,1,0])


results = index.search(
    [1,0,0,0],
    top_k=2
)

for r in results:

    print(r)