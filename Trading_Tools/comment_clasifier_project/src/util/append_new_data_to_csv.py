import pandas as pd
from src.logs.logger import logger  # Import your configured logger

def append_new_data_to_csv():
    """
    Append new data from an Excel file to an existing CSV file, filling missing values,
    and logging relevant processing steps.

    Reads new data from 'data/new_data.xlsx' and appends it to 'data/data.csv'.
    Missing values are filled (except for the 'comment' column) with empty strings.
    The updated data is saved back to 'data/data.csv'.

    Returns
    -------
    None
    """
    logger.info("Starting data append process.")

    # Load Excel file
    logger.info("Loading new data from 'data/new_data.xlsx'.")
    excel_data = pd.read_excel(
        r'data\new_data.xlsx',
        usecols=['source', 'date', 'curve_list', 'comment', 'grouping_var'],
        engine='openpyxl'
    )

    # Load existing CSV
    logger.info("Loading existing data from 'data/data.csv'.")
    csv_data = pd.read_csv(r'data/data.csv')

    # Combine
    logger.info("Combining new and existing data.")
    combined_data = pd.concat([csv_data, excel_data], ignore_index=True)

    # Log missing values count per column before filling
    missing_counts = combined_data.isna().sum()
    for col, missing_count in missing_counts.items():
        logger.info(f"Missing values before fill in column '{col}': {missing_count}")

    # Fill missing values (except 'comment')
    logger.info("Filling missing values (except for 'comment' column).")
    columns_to_fill = [col for col in combined_data.columns if col != 'comment']
    combined_data[columns_to_fill] = combined_data[columns_to_fill].fillna("")

    # Overwrite the original CSV
    combined_data.to_csv('data/data.csv', index=False)
    logger.info("Updated data saved to 'data/data.csv'.")

    logger.info("Data append process completed successfully.")
