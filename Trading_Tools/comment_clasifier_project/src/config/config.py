import json
from typing import Dict, Optional
from src.logs.logger import logger  # Import the logger

CONFIG_FILE = r'src\config\config.json'  # adjust path if needed

def load_config(filepath: str) -> Dict:
    """
    Load configuration data from a JSON file.

    Parameters
    ----------
    filepath : str
        Path to the JSON configuration file.

    Returns
    -------
    dict
        Dictionary containing the configuration data.
    """
    logger.info(f"Loading configuration from {filepath}.")
    with open(filepath, 'r') as f:
        config_data = json.load(f)
    logger.info("Configuration loaded successfully.")
    return config_data

CONFIG_DATA = load_config(CONFIG_FILE)
CLUSTER_LABEL_MAPPING: Dict[str, str] = CONFIG_DATA.get("cluster_label_mapping", {})

def load_mapping(filepath: str) -> Dict[str, str]:
    """
    Load the cluster label mapping. This function currently ignores the filepath 
    and returns the preloaded CLUSTER_LABEL_MAPPING.

    Parameters
    ----------
    filepath : str
        Path to the mapping file (ignored in this implementation).

    Returns
    -------
    dict
        The cluster label mapping dictionary.
    """
    logger.info("Loading cluster label mapping.")
    logger.info(f"Returning cluster label mapping with {len(CLUSTER_LABEL_MAPPING)} entries.")
    return CLUSTER_LABEL_MAPPING

def get_similarity_threshold() -> Optional[float]:
    """
    Retrieve the similarity threshold value from the configuration data.

    Returns
    -------
    Optional[float]
        The similarity threshold value, or None if not set.
    """
    logger.info("Retrieving similarity threshold.")
    similarity_threshold_section = CONFIG_DATA.get("similarity_threshold", {})
    threshold = similarity_threshold_section.get("01")
    logger.info(f"Similarity threshold retrieved: {threshold}")
    return threshold

def load_similarity_threshold() -> Optional[float]:
    """
    Compatibility function: same as get_similarity_threshold().

    Returns
    -------
    Optional[float]
        The similarity threshold value, or None if not set.
    """
    logger.info("Loading similarity threshold using compatibility function.")
    return get_similarity_threshold()
