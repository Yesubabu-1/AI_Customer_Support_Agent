import json

from config import MEMORY_FILE


class MemoryAgent:
    """
    Manages conversation history.
    """

    def __init__(self):
        self.memory_file = MEMORY_FILE

    def load_memory(self):
        """
        Load all previous conversations.
        """

        try:
            with open(
                self.memory_file,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):

            return []

    def save_memory(
        self,
        question,
        answer
    ):
        """
        Save one conversation.
        """

        history = self.load_memory()

        history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        with open(
            self.memory_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4
            )

    def get_recent_history(
        self,
        limit=5
    ):
        """
        Return last N conversations.
        """

        history = self.load_memory()

        return history[-limit:]

    def clear_memory(self):
        """
        Remove all conversation history.
        """

        with open(
            self.memory_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )