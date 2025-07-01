import json
import pandas as pd

def transform_to_flattened_excel(input_json: str, output_excel: str) -> None:
    """
    Transform hierarchical JSON comment data into a flattened Excel table.

    This function reads a JSON file that contains hierarchical comment data grouped by source, curve, and a grouping variable.
    It flattens the data into a tabular format where each row corresponds to a unique source-curve-grouping_var combination,
    and each comment is placed under its respective date column.

    Parameters
    ----------
    input_json : str
        The file path to the JSON file containing hierarchical comment data. The data should be grouped by source, curve, and
        grouping variable, and each comment should have a 'date', 'standard_label', and 'comment'.

    output_excel : str
        The file path where the flattened Excel table will be saved. The Excel file will contain the source, curve, grouping variable,
        and comments categorized under date columns.

    Returns
    -------
    None
        The function does not return any value. It writes the flattened data to an Excel file and prints a preview of the first few rows.

    Examples
    --------
    >>> transform_to_flattened_excel(
    >>>     input_json='comment_hierarchy.json',
    >>>     output_excel='Pivoted_Comments_Table.xlsx'
    >>> )

    Notes
    -----
    - Each comment in the Excel sheet is annotated with its label as "[label] comment".
    - Date columns in the Excel file are sorted chronologically.
    - The JSON input structure should be similar to the following example:

    >>> {
    >>>     "source1": {
    >>>         "curveA": {
    >>>             "USA": [
    >>>                 {"date": "2023-01-01", "standard_label": "Important", "comment": "Check this curve"},
    >>>                 {"date": "2023-02-01", "standard_label": "Note", "comment": "Update needed"}
    >>>             ]
    >>>         }
    >>>     }
    >>> }

    - Requires the `comment_hierarchy.json` file to be present in the working directory.
    """
    
    with open(input_json, 'r') as f:
        data = json.load(f)

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

# Example usage
transform_to_flattened_excel(
    input_json='comment_hierarchy.json',
    output_excel='Pivoted_Comments_Table.xlsx'
)
