from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)

def generate_embedding(text: str):
    """Generate an embedding for the given text."""
    return model.encode(text)