from sklearn.cluster import AgglomerativeClustering

def cluster_embeddings(embeddings, distance_threshold=1):
    clustering_model = AgglomerativeClustering(n_clusters=None, distance_threshold=distance_threshold)
    cluster_labels = clustering_model.fit_predict(embeddings)
    return cluster_labels
