import json
from typing import Dict
from typing import Optional

def load_mapping(filepath: str) -> Dict[str, str]:
    with open(filepath, 'r') as f:
        return json.load(f)

mapping_file = r"output\cluster_label_mapping.json"
CLUSTER_LABEL_MAPPING = load_mapping(mapping_file)

import json
from typing import Optional

def load_similarity_threshold() -> Optional[float]:
    """
    Reads the JSON file and returns the float value for the fixed key "01".

    Returns:
        The float value associated with the key "01", or None if key not found.
    """
    filepath = r'src\config\similarity_threshold.json'
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data.get("01")

