from abc import ABC, abstractmethod

class Retriever(ABC):
    @abstractmethod
    def retrieve(self, query_text: str, top_k: int):
        pass