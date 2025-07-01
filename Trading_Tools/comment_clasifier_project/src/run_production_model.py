import os
import pandas as pd
import pickle
import json
from src.util.convert_excel_to_csv import convert_excel_to_csv
from src.comment_clustering.preprocess import preprocess_comments
from src.comment_clustering.generate_embeddings import generate_embeddings
from src.comment_clustering.update_comment_hierarchy import update_comment_hierarchy
from src.comment_clustering.assign_labels_based_on_similarity import assign_labels_based_on_similarity
from src.config.config import load_similarity_threshold

def main():
    input_excel = r'data\test.xlsx'
    temp_csv = r'data\temp_csv.csv'
    pivot_output_path = r'output\pivoted_comments_table.xlsx'
    hierarchy_file = r'output\comment_hierarchy.json'
    embeddings_file = r'output\saved_embeddings.pkl'
    labels_file = r'output\saved_cluster_labels.pkl'  # Assuming saved labels are here
    cluster_to_label_file = r'output\cluster_label_mapping.json'
    
    # Step 1: Convert Excel to CSV
    convert_excel_to_csv(input_excel, temp_csv)

    # Step 2: Load new comments, preprocess, and generate embeddings
    df_new = pd.read_csv(temp_csv)
    df_new['comment'] = df_new['comment'].astype(str)
    df_new = preprocess_comments(df_new, comment_col='comment')
    new_embeddings = generate_embeddings(df_new['cleaned_comment'].tolist())

    # Step 3: Load existing embeddings and labels
    with open(embeddings_file, 'rb') as f:
        existing_embeddings = pickle.load(f)
    
    with open(labels_file, 'rb') as f:
        existing_labels = pickle.load(f)

    # Load cluster_to_label mapping (assuming it's a JSON file)
    with open(cluster_to_label_file, 'r') as f:
        cluster_to_label = json.load(f)

    # Step 4: Assign labels by similarity (pass the threshold as well)
    SIMILARITY_THRESHOLD = load_similarity_threshold()  # You can modify the threshold as needed
    assigned_labels = assign_labels_based_on_similarity(
        df_new, new_embeddings, existing_embeddings, existing_labels, cluster_to_label, threshold=SIMILARITY_THRESHOLD
    )

    # Step 5: Add the assigned labels to the dataframe
    df_new['standard_label'] = assigned_labels

    # Step 6: Update hierarchy JSON and pivot Excel
    update_comment_hierarchy(df_new, hierarchy_file, pivot_output_path)

    # Cleanup
    os.remove(temp_csv)

if __name__ == '__main__':
    main()
