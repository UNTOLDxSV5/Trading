from sklearn.cluster import AgglomerativeClustering
from src.logs.logger import logger  # Import logger

def cluster_embeddings(embeddings, distance_threshold=1):
    """
    Perform agglomerative clustering on a set of embeddings.
    ...
    """
    logger.info("Starting embedding clustering.")
    clustering_model = AgglomerativeClustering(n_clusters=None, distance_threshold=distance_threshold)
    cluster_labels = clustering_model.fit_predict(embeddings)
    logger.info("Embedding clustering completed.")
    return cluster_labels
