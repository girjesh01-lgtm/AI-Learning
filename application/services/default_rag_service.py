from llm.llm_client import LLMClient
from prompting.prompt_builder import PromptBuilder
from application.retrieval.retriever import Retriever
from application.services.rag_service import RagService


class DefaultRagService(RagService):
    def __init__(self, retriever: Retriever, prompt_builder: PromptBuilder, llm_client: LLMClient):
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.llm_client = llm_client


    def ask(self, query: str, top_k: int = 5) -> str:
        # Step 1: Retrieve relevant documents
        retrieved_docs = self.retriever.retrieve(query, top_k=top_k)

        # Step 2: Build the prompt using the retrieved documents
        prompt = self.prompt_builder.build(query, retrieved_docs)

        # Step 3: Generate a response using the LLM client
        response = self.llm_client.generate(prompt)

        return response