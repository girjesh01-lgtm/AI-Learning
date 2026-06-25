from llm_generation.llm_client import LLMClient
from models.prompt import Prompt


class FakeLLMClient(LLMClient):

    def generate_response(self, prompt: Prompt) -> str:
        return f"""
        ========= PROMPT RECEIVED =========

        {prompt.text}

        ==================================
        """