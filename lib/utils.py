import pandas as pd
from pathlib import Path
import os

def creat_folder(folder_path: str):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"📁 Created folder: {folder_path}")


def show(s: str):
    return s.replace("\n", "").strip()

def clear_lines(n=1):
    for _ in range(n):
        print("\033[A\033[K", end="")

def read_excel_files(folder_path):
    # Set the directory path
    directory = Path(folder_path)
    
    # List to store individual dataframes
    df_list = []

    # Iterate through all .xlsx and .xls files in the folder
    for file in directory.glob("*.xl*"):
        print(f"Reading: {file.name}")
        # Read the file and append it to our list
        temp_df = pd.read_excel(file)
        
        # Optional: Add a column to track which file the data came from
        temp_df['source_file'] = file.name
        
        df_list.append(temp_df)

    # Combine everything into one DataFrame
    if df_list:
        combined_df = pd.concat(df_list, ignore_index=True)
        return combined_df
    else:
        print("No Excel files found.")
        return None

    