import pandas as pd
from .logger import logger

def validate_data(df, required_columns, expected_dtypes):
    # Проверка наличия обязательных столбцов

    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        message = f"Отсутствуют обязательные столбцы: {missing_columns}"
        color = "#db8f8f"
        return message, color

    # Проверка типов данных

    df['MEAS_DT'] = pd.to_datetime(df['MEAS_DT'])

    for column, dtype in expected_dtypes.items():
        if not pd.api.types.is_dtype_equal(df[column].dtype, dtype):
            logger.info(f"{dtype}")

            # Удаляем угловые скобки, слово 'class', одинарные скобки из типа
            string_dtype = str(dtype).strip("<>").replace("class ", "")
            message = f"Неверный тип данных в столбце '{column}'. Ожидается '{string_dtype}', получено '{df[column].dtype}'"
            color = "#db8f8f"
            return message, color

    message = "Данные прошли валидацию успешно"
    color = "#82ed80"

    return message, color