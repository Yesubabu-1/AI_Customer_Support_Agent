from agents.memory_agent import MemoryAgent

memory = MemoryAgent()

memory.save_memory(
    "What is the refund policy?",
    "Refunds are available within 30 days."
)

memory.save_memory(
    "What are your business hours?",
    "Monday to Friday, 9 AM to 6 PM."
)

print(memory.get_recent_history())