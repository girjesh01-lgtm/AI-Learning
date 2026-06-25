from abc import ABC, abstractmethod

from models.search_result import SearchResult


class PromptBuilder(ABC):
    @abstractmethod
    def build_prompt(self, query: str, search_results: list[SearchResult]) -> str:
        """Builds a prompt string based on the provided arguments."""
        pass