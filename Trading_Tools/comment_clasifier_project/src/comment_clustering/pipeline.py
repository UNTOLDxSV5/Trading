import pandas as pd
import pickle
from src.comment_clustering.preprocess import preprocess_comments
from src.comment_clustering.generate_embeddings import generate_embeddings
from src.comment_clustering.cluster_embeddings import cluster_embeddings
from src.comment_clustering.mapping import map_clusters_to_labels, save_mapping, load_mapping
from src.comment_clustering.build_hierarchy import build_hierarchy, save_hierarchy
from src.logs.logger import logger  # Import the logger

def process_and_cluster_comments(
    input_csv: str,
    output_csv: str,
    embeddings_file: str,
    cluster_labels_file: str,
    mapping_file: str,
    hierarchy_file: str
) -> None:
    """
    Process a CSV file of comments, generate embeddings, cluster the embeddings, map clusters to labels,
    and build a hierarchy of the data. Saves intermediate and final results to specified output files.

    Parameters
    ----------
    input_csv : str
        Path to the input CSV file containing at least a 'comment' and 'date' column.
    output_csv : str
        Path to save the processed DataFrame with assigned cluster and standard labels.
    embeddings_file : str
        Path to save the generated embeddings as a pickle file.
    cluster_labels_file : str
        Path to save the cluster labels as a pickle file.
    mapping_file : str
        Path to the JSON file containing the cluster-to-label mapping.
    hierarchy_file : str
        Path to save the built hierarchy as a JSON file.

    Returns
    -------
    None
    """
    logger.info(f"Starting comment processing and clustering pipeline for {input_csv}.")

    # Load data
    logger.info("Loading data from CSV.")
    df = pd.read_csv(input_csv)
    df['comment'] = df['comment'].astype(str)

    # Preprocess
    logger.info("Preprocessing comments.")
    df = preprocess_comments(df, comment_col='comment')

    # Generate embeddings
    logger.info("Generating embeddings.")
    embeddings = generate_embeddings(df['cleaned_comment'].tolist())

    # Cluster
    logger.info("Clustering embeddings.")
    cluster_labels = cluster_embeddings(embeddings)
    df['cluster'] = cluster_labels

    # Map clusters
    logger.info(f"Loading cluster label mapping from {mapping_file}.")
    CLUSTER_LABEL_MAPPING = load_mapping(mapping_file)

    logger.info("Mapping cluster labels to standard labels.")
    df['standard_label'] = map_clusters_to_labels(cluster_labels, CLUSTER_LABEL_MAPPING)

    # Save embeddings and clusters
    logger.info(f"Saving embeddings to {embeddings_file}.")
    with open(embeddings_file, 'wb') as f:
        pickle.dump(embeddings, f)

    logger.info(f"Saving cluster labels to {cluster_labels_file}.")
    with open(cluster_labels_file, 'wb') as f:
        pickle.dump(cluster_labels, f)

    # Save DataFrame with labels
    logger.info(f"Saving processed DataFrame to {output_csv}.")
    df.to_csv(output_csv, index=False)

    # Sort by date
    logger.info("Sorting DataFrame by date.")
    df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)
    df = df.sort_values(by='date')

    # Build hierarchy and save
    logger.info("Building hierarchy.")
    hierarchy = build_hierarchy(df)
    logger.info(f"Saving hierarchy to {hierarchy_file}.")
    save_hierarchy(hierarchy, hierarchy_file)

    logger.info("Comment processing and clustering pipeline completed successfully.")
