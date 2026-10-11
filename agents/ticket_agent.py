import json
import os
from datetime import datetime

from config import TICKET_FILE


class TicketAgent:
    """
    Creates and manages customer support tickets.
    """

    def __init__(self):
        self.ticket_file = TICKET_FILE

    def load_tickets(self):
        """
        Load all existing tickets.
        """

        if not os.path.exists(self.ticket_file):
            return []

        with open(
            self.ticket_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def save_tickets(
        self,
        tickets
    ):
        """
        Save all tickets.
        """

        with open(
            self.ticket_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                tickets,
                file,
                indent=4
            )

    def generate_ticket_id(
        self,
        tickets
    ):
        """
        Generate the next ticket id.
        """

        return f"TKT-{len(tickets)+1:04d}"

    def create_ticket(
        self,
        customer_name,
        issue,
        priority="Medium"
    ):
        """
        Create a new support ticket.
        """

        tickets = self.load_tickets()

        ticket = {
            "ticket_id": self.generate_ticket_id(tickets),
            "customer_name": customer_name,
            "issue": issue,
            "priority": priority,
            "status": "Open",
            "created_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        tickets.append(ticket)

        self.save_tickets(tickets)

        return ticket

    def get_all_tickets(self):
        """
        Return all tickets.
        """

        return self.load_tickets()

    def get_ticket(
        self,
        ticket_id
    ):
        """
        Find a ticket by id.
        """

        tickets = self.load_tickets()

        for ticket in tickets:

            if ticket["ticket_id"] == ticket_id:

                return ticket

        return None

    def update_ticket_status(
        self,
        ticket_id,
        status
    ):
        """
        Update ticket status.
        """

        tickets = self.load_tickets()

        for ticket in tickets:

            if ticket["ticket_id"] == ticket_id:

                ticket["status"] = status

                self.save_tickets(tickets)

                return ticket

        return None