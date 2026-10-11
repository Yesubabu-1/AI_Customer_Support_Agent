import pickle

import faiss

from config import (
    CHUNKS_FILE,
    FAISS_INDEX_FILE
)

from models import EmbeddingModel


class VectorStore:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.index = None

        self.chunks = []

    def build_index(self, chunks):

        embeddings = self.embedding_model.create_embeddings(
            chunks
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

        self.chunks = chunks

    def save_index(self):

        faiss.write_index(
            self.index,
            FAISS_INDEX_FILE
        )

        with open(CHUNKS_FILE, "wb") as file:

            pickle.dump(self.chunks, file)

    def load_index(self):

        self.index = faiss.read_index(
            FAISS_INDEX_FILE
        )

        with open(CHUNKS_FILE, "rb") as file:

            self.chunks = pickle.load(file)

    def search(self, question, top_k):

        question_embedding = self.embedding_model.create_embeddings(
            [question]
        )

        distances, indices = self.index.search(
            question_embedding,
            top_k
        )

        retrieved_chunks = []

        retrieved_distances = []

        for distance, index in zip(
                distances[0],
                indices[0]
        ):

            if index < len(self.chunks):

                retrieved_chunks.append(
                    self.chunks[index]
                )

                retrieved_distances.append(
                    float(distance)
                )

        return {
            "chunks": retrieved_chunks,
            "distances": retrieved_distances
        }