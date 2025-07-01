import pandas as pd

def combine_files(excel_file: str, csv_file: str, output_file: str) -> None:
    """
    Combine data from an Excel file and a CSV file, then save the combined data to a new CSV file.

    Parameters
    ----------
    excel_file : str
        The file path of the Excel file to read. The Excel file must contain at least the following columns:
        'source', 'date', 'curve_list', 'comment', and 'grouping_var'.
    
    csv_file : str
        The file path of the CSV file to read. This file will be concatenated with the data from the Excel file.

    output_file : str
        The file path where the combined data will be saved as a CSV file.

    Returns
    -------
    None
        This function does not return any value. The combined data is written directly to the output file.
    
    Notes
    -----
    The Excel file is read using `pandas.read_excel()` and the CSV file using `pandas.read_csv()`.
    The function assumes that both files contain compatible data and will concatenate them along the rows
    (ignoring the index). The combined data is saved as a CSV file without including the index column.
    """
    excel_data = pd.read_excel(excel_file, usecols=['source', 'date', 'curve_list', 'comment', 'grouping_var'])

    csv_data = pd.read_csv(csv_file)

    combined_data = pd.concat([csv_data, excel_data], ignore_index=True)

    combined_data.to_csv(output_file, index=False)
    
    print(f"Files combined and saved as '{output_file}'")

combine_files('new.xlsx', 'data.csv', 'combined_data.csv')
