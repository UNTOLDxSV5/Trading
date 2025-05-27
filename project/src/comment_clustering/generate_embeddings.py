from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

def generate_embeddings(comments: List[str], model_name: str = 'all-MiniLM-L6-v2') -> np.ndarray:
    model = SentenceTransformer(model_name)
    embeddings = model.encode(comments, show_progress_bar=True)
    return embeddings
