from chunker import TextChunker
from config import COMPANY_DOCUMENT
from vector_store import VectorStore


chunker = TextChunker(
    COMPANY_DOCUMENT
)

chunks = chunker.create_chunks()

print(f"Total Chunks : {len(chunks)}")

vector_store = VectorStore()

vector_store.build_index(chunks)

vector_store.save_index()

print("FAISS Index Created Successfully")