from abc import ABC, abstractmethod

from models.prompt import Prompt


class LLMClient(ABC):
    
    @abstractmethod
    def generate_response(self, prompt: Prompt) -> str:
        """Generates a response based on the provided prompt."""
        pass