from abc import ABC, abstractmethod

class EmbeddingService(ABC):
    @abstractmethod
    def embed(self, text: str) -> list[float]:
        """
        Convert text into embedding vector
        """
        pass

    @abstractmethod
    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """
        Convert a batch of text into embedding vectors
        """
        pass