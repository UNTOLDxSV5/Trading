import json
from typing import Dict
import numpy as np
from src.config.config import load_mapping
from src.logs.logger import logger  # Import the logger

def map_clusters_to_labels(cluster_labels: np.ndarray, mapping: Dict[int, str]) -> list:
    """
    Map cluster labels to their corresponding textual labels using a provided mapping.

    Parameters
    ----------
    cluster_labels : numpy.ndarray of shape (n_samples,)
        An array of cluster labels to map.
    mapping : Dict[int, str]
        A dictionary mapping cluster label IDs to their textual descriptions.

    Returns
    -------
    list of str
        A list of textual labels corresponding to each cluster label. If a label is not found
        in the mapping, it defaults to 'Unknown'.
    """
    logger.info("Starting mapping of cluster labels to textual labels.")
    mapped_labels = [mapping.get(str(label), 'Unknown') for label in cluster_labels]
    logger.info("Mapping of cluster labels completed.")
    return mapped_labels

# Load the mapping from JSON file
mapping_file = r"output\cluster_label_mapping.json"
logger.info(f"Loading cluster label mapping from {mapping_file}.")
CLUSTER_LABEL_MAPPING = load_mapping(mapping_file)
logger.info(f"Cluster label mapping loaded successfully from {mapping_file}.")

def save_mapping(mapping: Dict[int, str], filepath: str) -> None:
    """
    Save a dictionary mapping of cluster labels to a JSON file.

    Parameters
    ----------
    mapping : Dict[int, str]
        The dictionary containing cluster label mappings to be saved.
    filepath : str
        The path to the output JSON file.

    Returns
    -------
    None
    """
    logger.info(f"Starting saving cluster label mapping to {filepath}.")
    with open(filepath, 'w') as f:
        json.dump(mapping, f, indent=2)
    logger.info(f"Cluster label mapping saved successfully to {filepath}.")