from config import CHUNK_SIZE, CHUNK_OVERLAP


class TextChunker:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_document(self):
      
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read().strip()

    def create_chunks(self):

        text = self.read_document()

        if not text:
            return []

        words = text.split()

        chunks = []

        step = CHUNK_SIZE - CHUNK_OVERLAP

        if step <= 0:
            raise ValueError(
                "CHUNK_OVERLAP must be smaller than CHUNK_SIZE."
            )

        for start in range(0, len(words), step):
            end = start + CHUNK_SIZE

            chunk = " ".join(words[start:end])

            if chunk.strip():
                chunks.append(chunk)

        return chunks