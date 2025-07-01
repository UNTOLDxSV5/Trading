"""
Convert an Excel file to a CSV file.

This script reads an Excel file (`t.xlsx`) using the `openpyxl` engine, then converts 
and saves it as a CSV file (`t.csv`). The index column is not included in the CSV file.

Parameters
----------
None

Returns
-------
None
    Converts the Excel file to a CSV file and prints a success message.

Examples
--------
>>> # Input Excel file: 't.xlsx'
>>> # Output CSV file: 't.csv'

>>> # The script reads the Excel file and saves the converted CSV:
>>> # ✅ Excel file converted to CSV
"""
import pandas as pd

# Load the Excel file
df = pd.read_excel('/content/t.xlsx', engine='openpyxl')

# Save to CSV
df.to_csv('t.csv', index=False)
print("✅ Excel file converted to CSV")
