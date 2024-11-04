import os
import pandas as pd

def combine_csv(dataframes, filename, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    full_path = os.path.join(folder, filename)
    if os.path.exists(full_path):
        os.remove(full_path)
    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df.to_csv(full_path, index=False)
    print(f"Data saved to {full_path}")

def into_csv(dataframe, filename, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    full_path = os.path.join(folder, filename)
    if os.path.exists(full_path):
        os.remove(full_path)
    dataframe.to_csv(full_path, index=False)
    print(f"Data saved to {full_path}")