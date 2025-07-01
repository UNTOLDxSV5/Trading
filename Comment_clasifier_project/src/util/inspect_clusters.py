from collections import defaultdict
from pathlib import Path
from src.logs.logger import logger  # Import your logger
import pandas as pd  # Ensure pandas is imported

def inspect_clusters(df, log_filename="cluster_inspection.txt") -> None:
    """
    Inspect clusters by writing unique cleaned comments from each cluster
    to a log file.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing at least 'cluster' and 'cleaned_comment' columns.
    log_filename : str, optional
        Name of the log file to save the inspection results. Default is
        'cluster_inspection.txt'.

    Returns
    -------
    None
    """
    logger.info("Starting cluster inspection process.")

    log_dir = Path(r"src\logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    
    log_path = log_dir / log_filename
    logger.info(f"Log file path: {log_path}")

    cluster_examples = defaultdict(set)  # unique comments per cluster

    logger.info("Collecting unique comments per cluster.")
    for _, row in df.iterrows():
        cluster = row['cluster']
        comment = row['cleaned_comment']
        if pd.notna(comment):  # only add non-NaN comments
            cluster_examples[cluster].add(comment)

    logger.info("Writing clusters to log file.")
    with open(log_path, 'w', encoding='utf-8') as f:
        for cluster in sorted(cluster_examples.keys()):
            f.write(f"\nCluster {cluster}:\n")
            for comment in sorted(cluster_examples[cluster]):
                f.write(f"{str(comment)}\n")  # safe write

    logger.info(f"Cluster inspection completed. Results saved to '{log_path}'.")
