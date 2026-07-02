from infrastructure.repository.inmemory_chunk_repository import InMemoryChunkRepository
from domain.chunk import Chunk
from domain.indexed_chunk import IndexedChunk

repo = InMemoryChunkRepository()

chunk = Chunk(
    chunk_id="c1",
    source_document_id="doc1",
    chunk_index=0,
    text="Hello World",
    metadata={}
)

indexed_chunk = IndexedChunk(
    chunk=chunk,
    embedding=[1.0, 2.0, 3.0]
)

repo.save(0, indexed_chunk)

result = repo.find_by_vector_id(0)

print(result)

repo.delete_by_vector_id(0)

print(repo.find_by_vector_id(0))