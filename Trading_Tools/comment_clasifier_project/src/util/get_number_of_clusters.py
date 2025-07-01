# utils.py
import numpy as np
from src.logs.logger import logger  # Import your logger

def get_number_of_clusters(labels: np.ndarray) -> int:
    """
    Calculate the number of unique clusters in the given labels.

    Parameters
    ----------
    labels : np.ndarray
        An array of cluster labels.

    Returns
    -------
    int
        The number of unique clusters present in the labels.
    """
    logger.info("Calculating number of unique clusters.")
    
    num_clusters = len(np.unique(labels))
    logger.info(f"Number of clusters found: {num_clusters}")
    
    return num_clusters
