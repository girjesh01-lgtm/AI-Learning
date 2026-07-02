from abc import ABC

from domain.chunk import Chunk
from domain.source_document import SourceDocument


class IngestionService(ABC):
    def ingest(self, source_document: SourceDocument) -> list[Chunk]:
        """
        Ingests a source document and returns a list of chunks.
        """
        pass

    def reingest(self, source_document: SourceDocument):
        """
        Re-ingests a source document, replacing any existing chunks.
        """
        pass
    