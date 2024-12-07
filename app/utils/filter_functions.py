from .logger import logger

def sort_columns(df):
    df_sorted = df.sort_index(axis=1)
    logger.info(df_sorted.columns.tolist())
    return df_sorted