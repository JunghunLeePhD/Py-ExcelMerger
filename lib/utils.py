import pandas as pd


def combine_files(files):
    try:
        dfs = [pd.read_excel(file.name) for file in files]
        return pd.concat(dfs, ignore_index=True)
    except Exception as _:
        return pd.DataFrame()
