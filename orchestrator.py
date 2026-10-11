from agents.knowledge_agent import KnowledgeAgent
from agents.memory_agent import MemoryAgent
from agents.data_validation_agent import DataValidationAgent
from agents.answer_agent import AnswerAgent
from agents.ticket_agent import TicketAgent
from agents.customer_feedback_agent import CustomerFeedbackAgent


class AIOrchestrator:
    """
    Manager Agent

    Coordinates all AI agents.
    """

    def __init__(self):

        self.knowledge_agent = KnowledgeAgent()

        self.memory_agent = MemoryAgent()

        self.validation_agent = DataValidationAgent()

        self.answer_agent = AnswerAgent()

        self.ticket_agent = TicketAgent()

        self.feedback_agent = CustomerFeedbackAgent()

    def process_query(
        self,
        question,
        customer_name="Anonymous"
    ):
       

       

        if not self.validation_agent.validate_question(question):

            return {
                "success": False,
                "message": "Invalid question."
            }

        history = self.memory_agent.get_recent_history()

        history_text = ""

        for item in history:

            history_text += (
                f"Customer: {item['question']}\n"
                f"Assistant: {item['answer']}\n\n"
            )

       

        knowledge = self.knowledge_agent.search(
            question
        )

        chunks = knowledge["chunks"]

        confidence = knowledge["confidence"]

       

        if self.validation_agent.validate_knowledge(
                confidence
        ):

            context = "\n\n".join(chunks)

            answer = self.answer_agent.generate_answer(
                question,
                context,
                history_text
            )

            self.memory_agent.save_memory(
                question,
                answer
            )

            return {
                "success": True,
                "type": "answer",
                "confidence": confidence,
                "answer": answer
            }

      
        ticket = self.ticket_agent.create_ticket(

            customer_name=customer_name,

            issue=question,

            priority="High"
        )

        return {
            "success": False,
            "type": "ticket",

            "message":
            "I couldn't confidently answer your question. A support ticket has been created.",

            "ticket": ticket
        }

    # ==================================================

    def submit_feedback(
        self,
        rating,
        comment
    ):

        if not self.validation_agent.validate_feedback(

                rating,
                comment
        ):

            return {

                "success": False,

                "message": "Invalid feedback."

            }

        feedback = self.feedback_agent.add_feedback(

            rating,

            comment
        )

        return {

            "success": True,

            "feedback": feedback

        }

   
    def get_feedback_statistics(self):

        return self.feedback_agent.get_feedback_statistics()

    

    def get_all_tickets(self):

        return self.ticket_agent.get_all_tickets()

   

    def get_ticket(
        self,
        ticket_id
    ):

        return self.ticket_agent.get_ticket(
            ticket_id
        )

   
    def update_ticket_status(
        self,
        ticket_id,
        status
    ):

        return self.ticket_agent.update_ticket_status(

            ticket_id,

            status
        )