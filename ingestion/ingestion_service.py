from abc import ABC

from models.chunk import Chunk
from models.source_document import SourceDocument


class IngestionService(ABC):
    def ingest(self, source_document: SourceDocument) -> list[Chunk]:
        """
        Ingests a source document and returns a list of chunks.
        """
        pass
    