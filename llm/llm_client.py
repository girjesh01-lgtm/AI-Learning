from abc import ABC, abstractmethod

from domain.prompt import Prompt


class LLMClient(ABC):
    
    @abstractmethod
    def generate(self, prompt: Prompt) -> str:
        """Generates a response based on the provided prompt."""
        pass