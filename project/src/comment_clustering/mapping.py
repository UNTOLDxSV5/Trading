import json
from typing import Dict
import numpy as np
from src.config.config import load_mapping
def map_clusters_to_labels(cluster_labels: np.ndarray, mapping: Dict[int, str]) -> list:
    return [mapping.get(str(label), 'Unknown') for label in cluster_labels]

# Load the mapping from JSON file
mapping_file = r"output\cluster_label_mapping.json"
CLUSTER_LABEL_MAPPING = load_mapping(mapping_file)


def save_mapping(mapping: Dict[int, str], filepath: str) -> None:
    with open(filepath, 'w') as f:
        json.dump(mapping, f, indent=2)
