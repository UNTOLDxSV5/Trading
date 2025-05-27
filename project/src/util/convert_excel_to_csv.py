import pandas as pd

def convert_excel_to_csv(excel_path: str, csv_path: str) -> None:
    """
    Convert an Excel file (.xlsx) to a CSV file.
    
    Args:
        excel_path (str): Path to the input Excel file.
        csv_path (str): Path where the converted CSV should be saved.
    """
    df = pd.read_excel(
        excel_path,
        usecols=['source', 'date', 'curve_list', 'comment', 'grouping_var'],
        engine='openpyxl'
    )
    df.to_csv(csv_path, index=False)
