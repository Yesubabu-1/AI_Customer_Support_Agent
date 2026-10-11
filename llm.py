import google.generativeai as genai

from config import GOOGLE_API_KEY


class GeminiModel:
    """
    Gemini LLM Wrapper
    """

    def __init__(self):

        genai.configure(api_key=GOOGLE_API_KEY)

        self.model = genai.GenerativeModel(
            "gemini-flash-latest"
        )

    def generate(self, prompt):

        response = self.model.generate_content(prompt)

        return response.text