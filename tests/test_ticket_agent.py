from agents.ticket_agent import TicketAgent

agent = TicketAgent()

ticket = agent.create_ticket(
    customer_name="Yesu Babu",
    issue="Unable to answer refund question",
    priority="High"
)

print(ticket)

print()

print(agent.get_all_tickets())