class ConversationMemory:
    """
    Stores conversation history.
    """

    def __init__(self):
        self.history = []

    def add_user_message(self, message):

        self.history.append({
            "role": "User",
            "message": message
        })

    def add_ai_message(self, message):

        self.history.append({
            "role": "Assistant",
            "message": message
        })

    def get_context(self):

        context = ""

        for item in self.history:

            context += (
                f"{item['role']}: "
                f"{item['message']}\n"
            )

        return context

    def clear(self):

        self.history.clear()