import pandas as pd
from src.logs.logger import logger  # Import your logger

def convert_excel_to_csv(excel_path: str, csv_path: str) -> None:
    """
    Convert an Excel file (.xlsx) to a CSV file.

    Parameters
    ----------
    excel_path : str
        Path to the input Excel file containing columns:
        ['source', 'date', 'curve_list', 'comment', 'grouping_var'].
    csv_path : str
        Path where the converted CSV file should be saved.

    Returns
    -------
    None
    """
    logger.info(f"Starting conversion from Excel to CSV.")
    logger.info(f"Reading Excel file: {excel_path}")
    
    df = pd.read_excel(
        excel_path,
        usecols=['source', 'date', 'curve_list', 'comment', 'grouping_var'],
        engine='openpyxl'
    )
    
    logger.info(f"Saving data to CSV file: {csv_path}")
    df.to_csv(csv_path, index=False)
    
    logger.info(f"Conversion completed successfully. Data saved to {csv_path}.")
