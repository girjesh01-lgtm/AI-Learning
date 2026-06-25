from models.prompt import Prompt
from models.search_result import SearchResult
from prompting.prompt_builder import PromptBuilder


class DefaultPromptBuilder(PromptBuilder):

    def build_prompt(self, query: str, search_results: list[SearchResult]) -> Prompt:

        """Builds a prompt string based on the provided arguments."""

        context = []
        
        for result in search_results:
            context.append(result.indexed_chunk.chunk.text)
        
        context_text = "\n\n".join(context)
        
        
        prompt_text = f"""you are a helpful assistant. 
        Answer only from the supplied context.
        If the answer cannot be found in the context, respond with "I don't know."
        context: {context_text}
        Question: {query}
        Answer:"""

        return Prompt(text=prompt_text.strip())