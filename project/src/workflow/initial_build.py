import pandas as pd
import re
from sentence_transformers import SentenceTransformer
from sklearn.cluster import AgglomerativeClustering
import json
import pickle
from collections import defaultdict

def process_and_cluster_comments(input_csv: str, output_csv: str, embeddings_file: str, cluster_labels_file: str, mapping_file: str, hierarchy_file: str) -> None:
    """
    Preprocess comments, generate embeddings, cluster them, and save results to multiple files.

    This function performs the following steps:
    1. Reads a CSV file with comments and preprocesses the 'comment' column.
    2. Generates sentence embeddings for the cleaned comments using a pre-trained transformer model.
    3. Performs agglomerative clustering on the embeddings to group similar comments together.
    4. Maps the cluster labels to standard categories and appends these labels to the original DataFrame.
    5. Saves the embeddings, cluster labels, and cluster-to-category mapping to pickle and JSON files.
    6. Sorts the DataFrame by 'date' and organizes the data into a hierarchical structure by source, curve, and grouping variable.
    7. Saves the hierarchical data to a JSON file.

    Parameters
    ----------
    input_csv : str
        The file path to the input CSV file containing the comments and other relevant columns.
        The CSV file must have at least the following columns: 'comment', 'date', 'source', 'curve_list', 'grouping_var'.

    output_csv : str
        The file path to save the DataFrame with added 'standard_label' column to a new CSV file.

    embeddings_file : str
        The file path to save the sentence embeddings (as a pickle file).

    cluster_labels_file : str
        The file path to save the cluster labels (as a pickle file).

    mapping_file : str
        The file path to save the cluster-to-category mapping (as a JSON file).

    hierarchy_file : str
        The file path to save the hierarchical structure of the comments (as a JSON file).

    Returns
    -------
    None
        This function does not return any value. It saves multiple files based on the processing.

    Notes
    -----
    - The comments are cleaned by removing punctuation, converting to lowercase, and stripping whitespace.
    - The sentence embeddings are computed using the 'all-MiniLM-L6-v2' model from Sentence-Transformers.
    - Agglomerative clustering is applied on the embeddings with a distance threshold of 1, producing clusters of similar comments.
    - The cluster labels are mapped to predefined categories, and the final output includes these labels.
    - The hierarchical JSON structure groups the data by source, curve, and grouping variable.

    Example
    -------
    process_and_cluster_comments(
        input_csv='/content/data.csv',
        output_csv='labeled_comments.csv',
        embeddings_file='saved_embeddings.pkl',
        cluster_labels_file='saved_cluster_labels.pkl',
        mapping_file='cluster_label_mapping.json',
        hierarchy_file='comment_hierarchy.json'
    )
    """
    
    df = pd.read_csv(input_csv)
    df['comment'] = df['comment'].astype(str)

    def pre_process(text_comment):
        if pd.isna(text_comment):
            return ""
        text_comment = text_comment.lower()
        text_comment = re.sub(r'[^\w\s]', '', text_comment)
        text_comment = text_comment.strip()
        return text_comment

    df['cleaned_comment'] = df['comment'].apply(pre_process)

    
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(df['cleaned_comment'].tolist(), show_progress_bar=True)

    
    clustering_model = AgglomerativeClustering(n_clusters=None, distance_threshold=1)
    cluster_labels = clustering_model.fit_predict(embeddings)
    df['cluster'] = cluster_labels

    
    cluster_label_mapping = {
        0: 'different_frequency',
        1: 'broker',
        2: 'raised_and_work_in_progress',
        3: 'discontinued_or_migrated',
        4: 'different_frequency',
        5: 'different_frequency',
        6: 'different_frequency',
        7: 'vendor',
        8: 'discontinued_or_migrated',
        9: 'broker',
        10: 'fixed',
        11: 'processor',
        12: 'processor',
        13: 'discontinued_or_migrated',
        14: 'publication_calendar',
        15: 'raised_and_work_in_progress',
        16: 'discontinued_or_migrated',
        17: 'different_frequency',
        18: 'discontinued_or_migrated',
        19: 'vendor',
        20: 'publication_calendar',
        21: 'publication_calendar',
        22: 'vendor',
        23: 'Not Reviewed / Evidenced',
        24: 'vendor',
        25: 'different_frequency',
        26: 'different_frequency',
        27: 'publication_calendar',
        28: 'trader',
        29: 'broker',
        30: 'publication_calendar',
        31: 'raised_and_work_in_progress',
        32: 'publication_calendar',
        33: 'publication_calendar',
        34: 'publication_calendar',
        35: 'publication_calendar',
        36: 'raised_and_work_in_progress',
        37: 'vendor',
        38: 'publication_calendar',
        39: 'publication_calendar',
        40: 'discontinued_or_migrated',
        41: 'publication_calendar',
        42: 'fixed',
        43: 'raised_and_work_in_progress',
        44: 'different_frequency',
        45: 'discontinued_or_migrated',
        46: 'discontinued_or_migrated',
        47: 'raised_and_work_in_progress',
        48: 'publication_calendar',
        49: 'raised_and_work_in_progress',
        50: 'raised_and_work_in_progress',
        51: 'raised_and_work_in_progress',
        52: 'publication_calendar',
        53: 'publication_calendar',
        54: 'discontinued_or_migrated',
        55: 'discontinued_or_migrated',
        56: 'broker',
        57: 'publication_calendar',
        -1: 'Not Reviewed / Evidenced'
    }

    df['standard_label'] = df['cluster'].map(cluster_label_mapping)

    
    with open(mapping_file, 'w') as f:
        json.dump(cluster_label_mapping, f)

    with open(embeddings_file, 'wb') as f:
        pickle.dump(embeddings, f)

    with open(cluster_labels_file, 'wb') as f:
        pickle.dump(cluster_labels, f)

    df.to_csv(output_csv, index=False)

    
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    df = df.sort_values(by='date')

    
    nested_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    for _, row in df.iterrows():
        comment = row['comment'] if pd.notna(row['comment']) and row['comment'].strip() != '' else '[Not Reviewed / Evidenced]'
        source = row['source']
        curve = row['curve_list']
        grouping_var = row['grouping_var']

        nested_dict[source][curve][grouping_var].append({
            'date': row['date'].strftime('%Y-%m-%d'),
            'comment': comment,
            'standard_label': row['standard_label']
        })

   
    with open(hierarchy_file, 'w') as f:
        json.dump(nested_dict, f, indent=2)


process_and_cluster_comments(
        input_csv=r'C:\Users\srini\OneDrive\Desktop\comment-classifier-project\data\data.csv',
        output_csv=r'C:\Users\srini\OneDrive\Desktop\comment-classifier-project\output\labeled_comments.csv',
        embeddings_file=r'C:\Users\srini\OneDrive\Desktop\comment-classifier-project\output\saved_embeddings.pkl',
        cluster_labels_file=r'C:\Users\srini\OneDrive\Desktop\comment-classifier-project\output\saved_cluster_labels.pkl',
        mapping_file=r'C:\Users\srini\OneDrive\Desktop\comment-classifier-project\output\cluster_label_mapping.json',
        hierarchy_file=r'C:\Users\srini\OneDrive\Desktop\comment-classifier-project\output\comment_hierarchy.json'
    )

