import json
import pandas as pd
from collections import defaultdict
from src.logs.logger import logger  # Import logger

def build_hierarchy(df: pd.DataFrame) -> dict:
    """
    Build a nested dictionary hierarchy from a pandas DataFrame.
    ...
    """
    logger.info("Starting hierarchy building.")
    nested_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    for idx, row in df.iterrows():
        logger.info(f"Processing row {idx}.")
        comment = row['comment'] if pd.notna(row['comment']) and row['comment'].strip() != '' else '[Not Reviewed / Evidenced]'
        source = row['source']
        curve = row['curve_list']
        grouping_var = row['grouping_var']

        nested_dict[source][curve][grouping_var].append({
            'date': row['date'].strftime('%Y-%m-%d') if pd.notna(row['date']) else None,
            'comment': comment,
            'standard_label': row['standard_label']
        })
    logger.info("Hierarchy building completed.")
    return nested_dict

def save_hierarchy(hierarchy: dict, filepath: str) -> None:
    """
    Save a nested dictionary hierarchy to a JSON file.
    ...
    """
    logger.info(f"Starting saving hierarchy to {filepath}.")
    with open(filepath, 'w') as f:
        json.dump(hierarchy, f, indent=2)
    logger.info(f"Hierarchy saved successfully to {filepath}.")
