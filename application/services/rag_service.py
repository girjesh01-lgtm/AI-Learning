from abc import ABC, abstractmethod


class RagService(ABC):

    @abstractmethod
    def ask(self, query: str, top_k: int = 5) -> str:
        pass