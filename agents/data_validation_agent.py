from config import CONFIDENCE_THRESHOLD


class DataValidationAgent:
  

    def validate_knowledge(self, confidence):
       
        return confidence >= CONFIDENCE_THRESHOLD

    def validate_ticket(
        self,
        customer_name,
        issue
    ):
       

        if not customer_name.strip():
            return False

        if not issue.strip():
            return False

        return True

    def validate_feedback(
        self,
        rating,
        comment
    ):
        

        if rating < 1 or rating > 5:
            return False

        if not comment.strip():
            return False

        return True

    def validate_question(
        self,
        question
    ):

        if not question.strip():
            return False

        return True