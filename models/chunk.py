from dataclasses import dataclass, field
from typing import Any


@dataclass
class Chunk:
    chunk_id: str
    source_document_id: str
    chunk_index: int
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)