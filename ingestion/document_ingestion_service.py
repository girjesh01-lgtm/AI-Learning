from ingestion.ingestion_service import IngestionService
from models.chunk import Chunk
from models.source_document import SourceDocument


class DocumentIngestionService(IngestionService):
    def __init__(self, chunker, indexer):
        self.chunker = chunker
        self.indexer = indexer

    def ingest(self, source_document: SourceDocument) -> list[Chunk]:
        chunks = self.chunker.chunk(source_document)
        self.indexer.index(chunks)
        return chunks
    
    def reingest(self, source_document: SourceDocument):
        self.indexer.delete_by_source_document(source_document.document_id)
        # Ingest the new version of the source document
        self.ingest(source_document)