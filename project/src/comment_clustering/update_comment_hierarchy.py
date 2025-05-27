import json
import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity

def load_embeddings(embeddings_file):
    with open(embeddings_file, 'rb') as f:
        return pickle.load(f)
    
def update_comment_hierarchy(new_comments_df, hierarchy_file, pivot_output_path):
    # Load existing hierarchy data
    try:
        with open(hierarchy_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # Ensure 'date' column is datetime
    new_comments_df['date'] = pd.to_datetime(new_comments_df['date'], errors='coerce')

    # Append new comments into hierarchy structure
    for _, row in new_comments_df.iterrows():
        comment = row['comment']
        source = row['source']
        curve = row['curve_list']
        grouping_var = row['grouping_var']
        label = row['standard_label']
        date = row['date'].strftime('%Y-%m-%d') if pd.notna(row['date']) else ''

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
    date_cols = sorted([col for col in df_pivot.columns if col not in non_date_cols])
    df_pivot = df_pivot[non_date_cols + date_cols]

    # Save the pivoted Excel
    df_pivot.to_excel(pivot_output_path, index=False)

    # Save updated hierarchy json
    with open(hierarchy_file, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Updated hierarchy saved to '{hierarchy_file}'")
    print(f"Pivoted comments saved to '{pivot_output_path}'")
