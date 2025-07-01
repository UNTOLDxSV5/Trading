import json
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from src.logs.logger import logger  # Import the logger

def load_embeddings(embeddings_file):
    """
    Load embeddings from a pickle file.

    Parameters
    ----------
    embeddings_file : str
        Path to the pickle file containing embeddings.

    Returns
    -------
    object
        The loaded embeddings object (typically a numpy.ndarray).
    """
    logger.info(f"Loading embeddings from {embeddings_file}.")
    with open(embeddings_file, 'rb') as f:
        embeddings = pickle.load(f)
    logger.info("Embeddings loaded successfully.")
    return embeddings

def update_comment_hierarchy(new_comments_df, hierarchy_file, pivot_output_path):
    """
    Update the comment hierarchy with new comments and generate a pivoted Excel file.

    Parameters
    ----------
    new_comments_df : pandas.DataFrame
        DataFrame containing new comments to add to the hierarchy.
    hierarchy_file : str
        Path to the existing JSON hierarchy file.
    pivot_output_path : str
        Path to save the pivoted Excel file.

    Returns
    -------
    None
    """
    logger.info(f"Starting update of comment hierarchy with new data.")
    
    # Load existing hierarchy data
    try:
        with open(hierarchy_file, 'r') as f:
            data = json.load(f)
        logger.info(f"Hierarchy loaded from {hierarchy_file}.")
    except FileNotFoundError:
        logger.warning(f"Hierarchy file {hierarchy_file} not found. Creating a new hierarchy.")
        data = {}

    # Ensure 'date' column is datetime
    new_comments_df['date'] = pd.to_datetime(new_comments_df['date'], errors='coerce')

    # Append new comments into hierarchy structure
    logger.info("Appending new comments to hierarchy structure.")
    for _, row in new_comments_df.iterrows():
        comment = row['comment']
        source = row['source']
        curve = row['curve_list']
        grouping_var = row['grouping_var']
        label = row['standard_label']
        date = row['date'].strftime('%Y-%m-%d') if pd.notna(row['date']) else ''

          # Skip if curve_list is missing or empty
        if pd.isna(curve) or str(curve).strip() == "":
            logger.warning(f"Skipping row with missing 'curve_list': {row.to_dict()}")
            continue

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

    # Create pivoted dataframe for Excel output
    logger.info("Generating pivoted DataFrame.")
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

    df_pivot = pd.DataFrame(records)

    # Sort columns: non-date first, then dates ascending
    non_date_cols = ['source', 'curve', 'grouping_var']
    date_cols = sorted([col for col in df_pivot.columns if col is not None and col not in non_date_cols])
    df_pivot = df_pivot[non_date_cols + date_cols]

    # Save the pivoted Excel
    logger.info(f"Saving pivoted comments to {pivot_output_path}.")
    df_pivot.to_excel(pivot_output_path, index=False)

    # Save updated hierarchy json
    logger.info(f"Saving updated hierarchy to {hierarchy_file}.")
    with open(hierarchy_file, 'w') as f:
        json.dump(data, f, indent=2)

    logger.info("Update of comment hierarchy completed successfully.")
    logger.info(f"Updated hierarchy saved to '{hierarchy_file}'.")
    logger.info(f"Pivoted comments saved to '{pivot_output_path}'.")
