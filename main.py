import pandas as pd
import os
from lib.utils import show, creat_folder, clear_lines, read_excel_files

def main():
    assets_path = "./assets"
    creat_folder(assets_path)

    print("\033c", end="") 
    print(f"--- 📂 Excel Processor: Reading from {assets_path} ---")
    
    try:
        df = read_excel_files(assets_path)
        if df is None or df.empty:
            print("❌ No data found. Please ensure Excel files are in the /assets/ folder.")
            return
    except Exception as e:
        print(f"❌ Error reading files: {e}")
        return

    cnames = list(df.columns)
    print(f"Found {len(cnames)} columns:\n" + "-"*30)
    
    for idx, cname in enumerate(cnames):
        print(f"{idx:3}: {show(cname)}")
        if (idx + 1) % 15 == 0 and idx != len(cnames) - 1:
            key = input("\n[Enter] for more, ['s'] to stop listing: ").strip().lower()
            clear_lines(2)
            if key == 's': break

    try:
        print("\n" + "-"*30)
        user_input = input("👉 Enter indices (ID first, then data columns): ")
        indices = [int(i) for i in user_input.split()]
        
        selected_cols = [cnames[i] for i in indices]
        group_key = selected_cols[0]
        data_cols = list(dict.fromkeys(selected_cols[1:])) 
    except (ValueError, IndexError):
        print("⚠️ Invalid selection.")
        return

    agg_rules = {}
    for col in data_cols:
        if pd.api.types.is_numeric_dtype(df[col]):
            agg_rules[col] = 'sum'
        else:
            agg_rules[col] = lambda x: x.mode().iat[0] if not x.mode().empty else None

    df_result = df.groupby(group_key).agg(agg_rules).reset_index()

    print("\n--- 👀 Result Preview (Top 5 Rows) ---")
    print(df_result.head())
    print("-" * 30)

    output_path = "./output"
    save_confirm = input(f"Save in {output_path} as csv? (y/n): ").strip().lower()
    if save_confirm == 'y':
        creat_folder(output_path, False)
        df_result.to_csv(f"{output_path}/result.csv", index=False)
        print("✅ Success! File saved.")
    else:
        print("❌ Save cancelled.")

if __name__ == "__main__":
    main()