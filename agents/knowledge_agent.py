from config import (
    TOP_K,
    CONFIDENCE_THRESHOLD
)

from vector_store import VectorStore


class KnowledgeAgent:
    """
    Searches the company knowledge base using RAG (FAISS).
    """

    def __init__(self):
        self.vector_store = VectorStore()
        self.vector_store.load_index()

    def search(self, question):
        """
        Search the vector database and return:
        - retrieved chunks
        - confidence score
        """

        result = self.vector_store.search(
            question,
            TOP_K
        )

        chunks = result["chunks"]
        distances = result["distances"]

        confidence = self.calculate_confidence(
            distances
        )

        return {
            "chunks": chunks,
            "confidence": confidence
        }

    def calculate_confidence(self, distances):
        """
        Converts FAISS distance into a confidence score.

        Lower distance = Higher confidence.
        """

        if not distances:
            return 0.0

        best_distance = min(distances)

        confidence = 1 / (1 + best_distance)

        return round(confidence, 2)

    def is_confident(self, confidence):
        """
        Checks whether the retrieved knowledge
        is good enough to answer.
        """

        return confidence >= CONFIDENCE_THRESHOLD