import os
from dotenv import load_dotenv

load_dotenv()


GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

COMPANY_DOCUMENT = "data/company_docs.txt"

CHUNK_SIZE = 100
CHUNK_OVERLAP = 20


TOP_K = 3

CONFIDENCE_THRESHOLD = 0.31

FAISS_INDEX_FILE = "data/index.faiss"
CHUNKS_FILE = "data/chunks.pkl"


MEMORY_FILE = "data/conversation_history.json"

TICKET_FILE = "data/tickets.json"

FEEDBACK_FILE = "data/feedback.json"