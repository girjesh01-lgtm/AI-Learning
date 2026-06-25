from llm_generation.llm_client import LLMClient
from prompting.prompt_builder import PromptBuilder
from retrieval.retriever import Retriever
from services.rag_service import RagService


class DefaultRagService(RagService):
    def __init__(self, retriever: Retriever, prompt_builder: PromptBuilder, llm_client: LLMClient, default_top_k: int = 3):
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.llm_client = llm_client
        self.default_top_k = default_top_k


    def ask(self, query: str) -> str:
        # Step 1: Retrieve relevant documents
        retrieved_docs = self.retriever.retrieve(query, top_k=self.default_top_k)

        # Step 2: Build the prompt using the retrieved documents
        prompt = self.prompt_builder.build_prompt(query, retrieved_docs)

        # Step 3: Generate a response using the LLM client
        response = self.llm_client.generate_response(prompt)

        return response