import pandas as pd
import pickle
from src.comment_clustering.preprocess import preprocess_comments
from src.comment_clustering.generate_embeddings import generate_embeddings
from src.comment_clustering.cluster_embeddings import cluster_embeddings
from src.comment_clustering.mapping import map_clusters_to_labels, save_mapping, load_mapping
from src.comment_clustering.build_hierarchy import build_hierarchy, save_hierarchy


def process_and_cluster_comments(
    input_csv: str,
    output_csv: str,
    embeddings_file: str,
    cluster_labels_file: str,
    mapping_file: str,
    hierarchy_file: str
) -> None:


    # Load data
    df = pd.read_csv(input_csv)
    df['comment'] = df['comment'].astype(str)

    # Preprocess
    df = preprocess_comments(df, comment_col='comment')

    # Generate embeddings
    embeddings = generate_embeddings(df['cleaned_comment'].tolist())

    # Cluster
    cluster_labels = cluster_embeddings(embeddings)
    df['cluster'] = cluster_labels

    # Map clusters
    # Load mapping from JSON
    CLUSTER_LABEL_MAPPING = load_mapping(mapping_file)

# Map cluster labels to standard labels
    df['standard_label'] = map_clusters_to_labels(cluster_labels, CLUSTER_LABEL_MAPPING)

    # Save embeddings and clusters as pickle
    with open(embeddings_file, 'wb') as f:
        pickle.dump(embeddings, f)

    with open(cluster_labels_file, 'wb') as f:
        pickle.dump(cluster_labels, f)

    # Save dataframe with labels to CSV
    df.to_csv(output_csv, index=False)

    # Sort by date
    df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)
    df = df.sort_values(by='date')

    # Build hierarchy and save
    hierarchy = build_hierarchy(df)
    save_hierarchy(hierarchy, hierarchy_file)
