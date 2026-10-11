from llm import GeminiModel


class AnswerAgent:
   

    def __init__(self):
        self.llm = GeminiModel()

    def generate_answer(
        self,
        question,
        knowledge_context,
        conversation_history
    ):

        prompt = f"""
You are an AI Customer Support Assistant.

Your responsibilities:

1. Answer ONLY using the provided Company Knowledge.
2. Use the Conversation History only for context.
3. Do NOT make up information.
4. If the answer is not found in the Company Knowledge, reply exactly:

"I couldn't find this information in the company documentation."

----------------------------------------------------

Conversation History

{conversation_history}

----------------------------------------------------

Company Knowledge

{knowledge_context}

----------------------------------------------------

Customer Question

{question}

----------------------------------------------------

Answer:
"""

        return self.llm.generate(prompt)