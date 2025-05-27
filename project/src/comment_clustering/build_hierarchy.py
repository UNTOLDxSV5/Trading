import json
import pandas as pd
from collections import defaultdict

def build_hierarchy(df: pd.DataFrame) -> dict:
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
    return nested_dict

def save_hierarchy(hierarchy: dict, filepath: str) -> None:
    with open(filepath, 'w') as f:
        json.dump(hierarchy, f, indent=2)
