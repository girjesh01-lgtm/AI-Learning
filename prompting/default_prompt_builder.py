from domain.prompt import Prompt
from domain.search_result import SearchResult
from prompting.prompt_builder import PromptBuilder


class DefaultPromptBuilder(PromptBuilder):

    def build(self, query: str, search_results: list[SearchResult]) -> Prompt:

        """Builds a prompt string based on the provided arguments."""

        lines = []

        lines.append(
            "You are a helpful assistant."
        )

        lines.append(
            "Answer the question using ONLY the provided context."
        )

        lines.append(
            "If the answer is not present, reply:"
        )

        lines.append(
            "\"I don't know based on the provided documents.\""
        )

        lines.append("")
        lines.append("Context:")
        lines.append("")

        for index, result in enumerate(search_results, start=1):

            lines.append(
                f"Chunk {index}:"
            )

            lines.append(
                result.chunk.text
            )

            lines.append("")


        lines.append(
        "Question:"
        )

        lines.append(
            query
        )

        lines.append("")
        lines.append("Answer:")

        return Prompt(
            text="\n".join(lines)
        )