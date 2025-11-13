import pandas as pd
import os

EXCEL_FILE_PATH = 'INGRES DATABASE.xlsx'
# 🔑 CRITICAL FIX: Explicitly list ONLY the raw data sheets to load. 
# This ensures the new 'Calculations' (pivot table) sheet is ignored.
DATA_SHEET_NAMES = ['2025', '2024', '2023', '2022', '2020'] 

try:
    # Load ONLY the specified data sheets
    ingres_data_dict = pd.read_excel(EXCEL_FILE_PATH, sheet_name=DATA_SHEET_NAMES)
    
    # Check the new keys to confirm the sheet names
    print("Successfully loaded INGRES data from data sheets!")
    print(f"Loaded sheet names (keys): {list(ingres_data_dict.keys())}") 

    # Verify the latest sheet
    latest_year = DATA_SHEET_NAMES[0] # Assumes the first in the list is the latest
    if latest_year in ingres_data_dict:
        latest_year_df = ingres_data_dict[latest_year]
        print(f"\nData for {latest_year} (first 5 rows):\n{latest_year_df.head()}")
    else:
        print(f"\nError: Latest sheet '{latest_year}' was not found in the loaded data.")
    
except FileNotFoundError:
    print(f"Error: The file '{EXCEL_FILE_PATH}' was not found. Check the file name and path.")
except Exception as e:
    print(f"An error occurred while reading the Excel file: {e}")
