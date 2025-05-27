import pandas as pd
import logging

# Configure logging (you can customize level and file path)
logging.basicConfig(
    filename=r'src\logs\data_append.log',
    filemode='a',  # append mode
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def append_new_data_to_csv():
    # Load Excel file
    excel_data = pd.read_excel(
        r'data\new_data.xlsx',
        usecols=['source', 'date', 'curve_list', 'comment', 'grouping_var'],
        engine='openpyxl'
    )

    # Load existing CSV
    csv_data = pd.read_csv(r'data/data.csv')

    # Combine
    combined_data = pd.concat([csv_data, excel_data], ignore_index=True)

    # Log missing values count per column before filling
    missing_counts = combined_data.isna().sum()
    for col, missing_count in missing_counts.items():
        logging.info(f"Missing values before fill in column '{col}': {missing_count}")

    # Fill missing values (except 'comment')
    columns_to_fill = [col for col in combined_data.columns if col != 'comment']
    combined_data[columns_to_fill] = combined_data[columns_to_fill].fillna("Not Reviewed / Evidenced")

    # Overwrite the original CSV
    combined_data.to_csv('data/data.csv', index=False)

    logging.info("Updated data saved to 'data/data.csv'.")
