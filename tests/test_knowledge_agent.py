from agents.knowledge_agent import KnowledgeAgent

agent = KnowledgeAgent()

result = agent.search(
    "What is the refund policy?"
)

print(result)