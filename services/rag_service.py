from abc import ABC, abstractmethod


class RagService(ABC):

    @abstractmethod
    def ask(self, query: str) -> str:
        pass