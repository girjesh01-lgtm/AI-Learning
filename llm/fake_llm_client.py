from llm.llm_client import LLMClient
from domain.prompt import Prompt


class FakeLLMClient(LLMClient):

    def generate(self, prompt: Prompt) -> str:
        return (
            "This is a fake response.\n\n"
            "Prompt received:\n\n"
            f"{prompt.text}"
        )