from agents.answer_agent import AnswerAgent

agent = AnswerAgent()

history = """
Customer:
Hi

Assistant:
Hello! How can I help you?
"""

knowledge = """
Refund Policy

Customers can return products within 30 days.

Refunds are processed within 5 business days.
"""

answer = agent.generate_answer(
    "What is the refund policy?",
    knowledge,
    history
)

print(answer)