from agents.data_validation_agent import DataValidationAgent

validator = DataValidationAgent()

print("Knowledge:", validator.validate_knowledge(0.85))

print("Question:", validator.validate_question(
    "What is the refund policy?"
))

print("Ticket:", validator.validate_ticket(
    "John",
    "Refund not received"
))

print("Feedback:", validator.validate_feedback(
    5,
    "Excellent support"
))