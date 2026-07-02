from abc import ABC, abstractmethod

from domain.prompt import Prompt
from domain.search_result import SearchResult


class PromptBuilder(ABC):
    @abstractmethod
    def build(self, query: str, search_results: list[SearchResult]) -> Prompt:
        """Builds a prompt string based on the provided arguments."""
        pass