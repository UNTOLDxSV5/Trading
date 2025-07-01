from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np
from src.logs.logger import logger  # Import logger

def generate_embeddings(comments: List[str], model_name: str = 'all-MiniLM-L6-v2') -> np.ndarray:
    """
    Generate embeddings for a list of textual comments using a pre-trained SentenceTransformer model.
    ...
    """
    logger.info(f"Starting embedding generation using model '{model_name}'.")
    model = SentenceTransformer(model_name)
    embeddings = model.encode(comments, show_progress_bar=True)
    logger.info("Embedding generation completed.")
    return embeddings
