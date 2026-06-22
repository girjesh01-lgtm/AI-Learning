from abc import ABC, abstractmethod

from models.chunk import Chunk
from models.source_document import SourceDocument


class Chunker(ABC):
    @abstractmethod
    def chunk(self, source_document: SourceDocument) -> list[Chunk]:
        pass