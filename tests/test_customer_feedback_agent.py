from agents.customer_feedback_agent import CustomerFeedbackAgent

agent = CustomerFeedbackAgent()

feedback = agent.add_feedback(
    rating=5,
    comment="Excellent support."
)

print(feedback)

print()

print(agent.get_feedback_statistics())