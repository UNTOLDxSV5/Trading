import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json
import pandas as pd

def assign_labels_based_on_similarity(df_new, new_embeddings, existing_embeddings, existing_labels, cluster_to_label, threshold):
    """
    Assign labels to new comments based on cosine similarity to existing comment embeddings.
    
    Parameters:
    - df_new (pd.DataFrame): DataFrame containing the new comments and other metadata.
    - new_embeddings (np.ndarray): Embeddings of the new comments.
    - existing_embeddings (np.ndarray): Embeddings of the existing comments.
    - existing_labels (list): Labels of the existing comments (corresponding to clusters).
    - cluster_to_label (dict): A dictionary that maps cluster labels to human-readable labels.
    - threshold (float): Cosine similarity threshold to classify as 'Not Reviewed / Evidenced' if below this value.
    
    Returns:
    - new_labels (list): List of labels assigned to new comments.
    """
    
    # Initialize list to store new labels
    new_labels = []

    # Iterate over new embeddings and assign labels based on cosine similarity
    for new_embedding, comment in zip(new_embeddings, df_new['comment']):
        # Check if the comment is empty or NaN
        if pd.isna(comment) or comment.strip() == "" or comment=="nan":
            new_label = "Not Reviewed / Evidenced"
        else:
            # Calculate cosine similarity between the new embedding and existing embeddings
            cos_similarity = cosine_similarity([new_embedding], existing_embeddings)
            
            # Find the index of the most similar existing embedding
            closest_idx = np.argmax(cos_similarity)
            
            # If the maximum cosine similarity is below the threshold, classify as 'Not Reviewed / Evidenced'
            if cos_similarity[0][closest_idx] < threshold:
                new_label = "Not Reviewed / Evidenced"
            else:
                # Otherwise, use the cluster label for the closest embedding
                closest_cluster = existing_labels[closest_idx]
                new_label = cluster_to_label.get(str(closest_cluster), "Not Reviewed / Evidenced")
        
        # Append the assigned label to the new_labels list
        new_labels.append(new_label)

    return new_labels
