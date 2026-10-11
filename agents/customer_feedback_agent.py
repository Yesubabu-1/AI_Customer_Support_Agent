import json
import os
from datetime import datetime

from config import FEEDBACK_FILE


class CustomerFeedbackAgent:
    """
    Stores and analyzes customer feedback.
    """

    def __init__(self):
        self.feedback_file = FEEDBACK_FILE

    def load_feedback(self):

        if not os.path.exists(self.feedback_file):
            return []

        with open(
            self.feedback_file,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    def save_feedback_data(
        self,
        feedback_list
    ):

        with open(
            self.feedback_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                feedback_list,
                file,
                indent=4
            )

    def add_feedback(
        self,
        rating,
        comment
    ):
        """
        Save customer feedback.
        """

        feedback_list = self.load_feedback()

        feedback = {
            "feedback_id": len(feedback_list) + 1,
            "rating": rating,
            "comment": comment,
            "created_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        }

        feedback_list.append(feedback)

        self.save_feedback_data(feedback_list)

        return feedback

    def get_all_feedback(self):

        return self.load_feedback()

    def get_feedback_statistics(self):

        feedback = self.load_feedback()

        if len(feedback) == 0:

            return {
                "total_feedback": 0,
                "average_rating": 0
            }

        total_rating = sum(
            item["rating"]
            for item in feedback
        )

        average = round(
            total_rating / len(feedback),
            2
        )

        return {
            "total_feedback": len(feedback),
            "average_rating": average
        }