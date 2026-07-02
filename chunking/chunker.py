from abc import ABC, abstractmethod

from domain.chunk import Chunk
from domain.source_document import SourceDocument


class Chunker(ABC):
    @abstractmethod
    def chunk(self, source_document: SourceDocument) -> list[Chunk]:
        pass