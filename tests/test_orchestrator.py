from orchestrator import AIOrchestrator

orchestrator = AIOrchestrator()

response = orchestrator.process_query(
    question="What is the refund policy?",
    customer_name="Yesu Babu"
)

print(response)