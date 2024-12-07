from .logger import logger

def sort_columns(df):
    df_sorted = df.sort_index(axis=1)
    return df_sorted