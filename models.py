from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def create_embeddings(self, texts):
        """
        Generate embeddings for a list of texts.
        """
        return self.model.encode(
            texts,
            convert_to_numpy=True
        )