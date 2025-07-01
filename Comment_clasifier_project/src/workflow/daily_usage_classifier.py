import pandas as pd
import json
import re
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def classify_and_save_new_comments(input_csv: str, 
                                   output_excel: str, 
                                   saved_embeddings_file: str, 
                                   saved_cluster_labels_file: str, 
                                   cluster_label_mapping_file: str, 
                                   hierarchy_file: str) -> None:
    """
    Classify and save new comments to an Excel file based on pre-trained embeddings.

    This function loads pre-trained comment embeddings, cluster labels, and a label mapping, 
    then classifies a new set of comments based on cosine similarity. The new comments are 
    preprocessed, embedded, and compared against the saved embeddings to determine their 
    closest cluster. The function generates a new table with comments and their corresponding 
    labels, then saves the results in an Excel file (`Pivoted_Comments_Table.xlsx`). The 
    updated comment hierarchy is also written back to a JSON file (`comment_hierarchy.json`).

    Parameters
    ----------
    input_csv : str
        The file path to the CSV file containing new comments. This file should include columns 
        for 'comment', 'source', 'curve_list', 'grouping_var', and 'date'.
    
    output_excel : str
        The file path where the new Excel table with classified comments will be saved. 
        The table will include columns for source, curve, grouping_var, date, standard_label, and 
        each date that appears in the comment hierarchy.

    saved_embeddings_file : str
        The file path to the pickle file containing the pre-trained embeddings for the original comments.

    saved_cluster_labels_file : str
        The file path to the pickle file containing the cluster labels corresponding to the pre-trained embeddings.

    cluster_label_mapping_file : str
        The file path to the JSON file containing the mapping between cluster labels and human-readable categories.

    hierarchy_file : str
        The file path to the JSON file containing the current comment hierarchy. This file will be updated with the new classified comments.

    Returns
    -------
    None
        The function does not return any value. It writes the classified comments to an Excel file and updates 
        the `comment_hierarchy.json` file.

    Examples
    --------
    >>> classify_and_save_new_comments(
    >>>     input_csv='/content/t.csv',
    >>>     output_excel='Pivoted_Comments_Table.xlsx',
    >>>     saved_embeddings_file='saved_embeddings.pkl',
    >>>     saved_cluster_labels_file='saved_cluster_labels.pkl',
    >>>     cluster_label_mapping_file='cluster_label_mapping.json',
    >>>     hierarchy_file='comment_hierarchy.json'
    >>> )
    
    Notes
    -----
    - The function uses a pre-trained sentence transformer model (`all-MiniLM-L6-v2`) to generate embeddings for new comments.
    - Cosine similarity is used to match new comments with saved embeddings, and a similarity threshold of 0.3 is applied to classify comments.
    - The input CSV should contain the following columns: 'comment', 'source', 'curve_list', 'grouping_var', and 'date'.
    - The output Excel file will have columns for source, curve, grouping variable, date, and standard label, along with comments under respective date columns.
    - The resulting hierarchy will be written to `comment_hierarchy.json`, which organizes the comments by source, curve, and grouping variable.
    """
    
    model = SentenceTransformer('all-MiniLM-L6-v2')

    with open(saved_embeddings_file, 'rb') as f:
        saved_embeddings = pickle.load(f)

    with open(saved_cluster_labels_file, 'rb') as f:
        saved_cluster_labels = pickle.load(f)

    with open(cluster_label_mapping_file, 'r') as f:
        cluster_to_label = json.load(f)

    new_comments_df = pd.read_csv(input_csv)
    print(new_comments_df.columns)

    new_comments_df.rename(columns=lambda x: x.strip(), inplace=True)
    if 'comment' not in new_comments_df.columns:
        raise KeyError("The 'comment' column is missing from the input data.")

    def preprocess(text):
        if pd.isna(text):
            return ""
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        text = text.strip()
        return text

    new_comments_df['cleaned_comment'] = new_comments_df['comment'].apply(preprocess)

    new_embeddings = model.encode(new_comments_df['cleaned_comment'].tolist(), show_progress_bar=True)

    SIMILARITY_THRESHOLD = 0.3

    new_labels = []

    for new_embedding, comment in zip(new_embeddings, new_comments_df['comment']):
        if pd.isna(comment) or comment.strip() == "":
            new_comment_label = "Not Reviewed / Evidenced"
        else:
            cos_similarity = cosine_similarity([new_embedding], saved_embeddings)
            closest_idx = np.argmax(cos_similarity)
            max_cos_similarity = cos_similarity[0][closest_idx]
            if max_cos_similarity < SIMILARITY_THRESHOLD:
                new_comment_label = "Not Reviewed / Evidenced"
            else:
                new_comment_cluster = saved_cluster_labels[closest_idx]
                new_comment_label = cluster_to_label.get(str(new_comment_cluster))
        new_labels.append(new_comment_label)

    new_comments_df['standard_label'] = new_labels

    with open(hierarchy_file, 'r') as f:
        data = json.load(f)

    new_comments_df['date'] = pd.to_datetime(new_comments_df['date'], errors='coerce')

    for _, row in new_comments_df.iterrows():
        comment = row['comment']
        source = row['source']
        curve = row['curve_list']
        grouping_var = row['grouping_var']
        label = row['standard_label']
        if pd.notna(row['date']):
            date = row['date'].strftime('%Y-%m-%d')
        else:
            date = ''
        if source not in data:
            data[source] = {}
        if curve not in data[source]:
            data[source][curve] = {}
        if grouping_var not in data[source][curve]:
            data[source][curve][grouping_var] = []
        data[source][curve][grouping_var].append({
            'date': date,
            'comment': comment,
            'standard_label': label
        })

    records = []

    for source, curves in data.items():
        for curve, groups in curves.items():
            for grouping_var, comments in groups.items():
                row = {'source': source, 'curve': curve, 'grouping_var': grouping_var}
                for entry in comments:
                    date = entry['date']
                    label = entry['standard_label']
                    comment = entry['comment']
                    row[date] = f"[{label}] {comment}"
                records.append(row)

    df = pd.DataFrame(records)

    non_date_cols = ['source', 'curve', 'grouping_var']
    date_cols = sorted([col for col in df.columns if col not in non_date_cols])
    df = df[non_date_cols + date_cols]

    df.to_excel(output_excel, index=False)

    print(df.head())

    with open(hierarchy_file, 'w') as f:
        json.dump(data, f, indent=2)

    print("New comments classified and saved to 'Pivoted_Comments_Table.xlsx'!")
