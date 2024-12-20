import pandas as pd
from .logger import logger

def validate_data(df):
    # Проверка наличия обязательных столбцов
    required_columns = [
        "MEAS_DT", "Cu_oreth", "Ni_oreth", "Ore_mass", "Mass_1", "Mass_2", "Dens_4", "Mass_4", "Vol_4", "Cu_4F",
        "Ni_4F", "Ni_4.1C", "Ni_4.1C_max", "Ni_4.1C_min", "Ni_4.1T", "Ni_4.1T_max", "Ni_4.1T_min", "FM_4.1_A", "Ni_4.2C",
        "Ni_4.2C_max", "Ni_4.2C_min", "Ni_4.2T", "Ni_4.2T_max", "Ni_4.2T_min", "FM_4.2_A", "Dens_5", "Mass_5", "Vol_5", "Ni_5F",
        "Ni_5.1C", "Ni_5.1C_max", "Ni_5.1C_min", "Ni_5.1T", "Ni_5.1T_max", "Ni_5.1T_min", "FM_5.1_A", "Ni_5.2C", "Ni_5.2C_max",
        "Ni_5.2C_min", "Ni_5.2T", "Ni_5.2T_max", "Ni_5.2T_min", "FM_5.2_A", "Dens_6", "Mass_6", "Vol_6", "Ni_6F", "Ni_6.1C",
        "Ni_6.1C_max", "Ni_6.1C_min", "Ni_6.1T", "Ni_6.1T_max", "Ni_6.1T_min", "FM_6.1_A", "Ni_6.2C", "Ni_6.2C_max", "Ni_6.2C_min",
        "Ni_6.2T", "Ni_6.2T_max", "Ni_6.2T_min", "FM_6.2_A", "Cu_resth", "Ni_resth", "Cu_1.1C", "Ni_1.1C", "Cu_1.2C", "Ni_1.2C",
        "Cu_2F", "Ni_2F", "Cu_2.1C", "Ni_2.1C", "Cu_2.2C", "Ni_2.2C", "Cu_3F", "Ni_3F", "Cu_3.1C", "Ni_3.1C", "Cu_3.2C", "Ni_3.2C",
        "Cu_2.1T", "Ni_2.1T", "Cu_2.2T", "Ni_2.2T", "Cu_3.1T", "Ni_3.1T", "Cu_3.2T", "Ni_3.2T", "Dens_3", "Dens_1", "Dens_2", "Mass_3",
        "FM_1.1_A", "Cu_1.1C_max", "Cu_1.1C_min", "Ni_1.1C_max", "Ni_1.1C_min", "Ni_1.1T_max", "Ni_1.1T_min", "FM_1.2_A", "Cu_1.2C_max",
        "Cu_1.2C_min", "Ni_1.2C_max", "Ni_1.2C_min", "Ni_1.2T_max", "Ni_1.2T_min", "FM_2.1_A", "Cu_2.1C_max", "Cu_2.1C_min", "Cu_2.1T_max",
        "Cu_2.1T_min", "FM_2.2_A", "Cu_2.2C_max", "Cu_2.2C_min", "Cu_2.2T_max", "Cu_2.2T_min", "FM_3.1_A", "Cu_3.1C_max", "Cu_3.1C_min",
        "Ni_3.1C_max", "Ni_3.1C_min", "Cu_3.1T_max", "Cu_3.1T_min", "FM_3.2_A", "Cu_3.2C_max", "Cu_3.2C_min", "Ni_3.2C_max", "Ni_3.2C_min",
        "Cu_3.2T_max", "Cu_3.2T_min", "Ni_rec"
    ]

    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        message = f"Отсутствуют обязательные столбцы: {missing_columns}"
        color = "#db8f8f"
        return message, color

    # Проверка типов данных

    df['MEAS_DT'] = pd.to_datetime(df['MEAS_DT'])
    expected_dtypes = {
        "MEAS_DT": "datetime64[ns]",
        "Cu_oreth": "float",
        "Ni_oreth": "float",
        "Ore_mass": "float",
        "Mass_1": "float",
        "Mass_2": "float",
        "Dens_4": "float",
        "Mass_4": "float",
        "Vol_4": "float",
        "Cu_4F": "float",
        "Ni_4F": "float",
        "Ni_4.1C": "float",
        "Ni_4.1C_max": "float",
        "Ni_4.1C_min": "float",
        "Ni_4.1T": "float",
        "Ni_4.1T_max": "float",
        "Ni_4.1T_min": "float",
        "FM_4.1_A": "float",
        "Ni_4.2C": "float",
        "Ni_4.2C_max": "float",
        "Ni_4.2C_min": "float",
        "Ni_4.2T": "float",
        "Ni_4.2T_max": "float",
        "Ni_4.2T_min": "float",
        "FM_4.2_A": "float",
        "Dens_5": "float",
        "Mass_5": "float",
        "Vol_5": "float",
        "Ni_5F": "float",
        "Ni_5.1C": "float",
        "Ni_5.1C_max": "float",
        "Ni_5.1C_min": "float",
        "Ni_5.1T": "float",
        "Ni_5.1T_max": "float",
        "Ni_5.1T_min": "float",
        "FM_5.1_A": "float",
        "Ni_5.2C": "float",
        "Ni_5.2C_max": "float",
        "Ni_5.2C_min": "float",
        "Ni_5.2T": "float",
        "Ni_5.2T_max": "float",
        "Ni_5.2T_min": "float",
        "FM_5.2_A": "float",
        "Dens_6": "float",
        "Mass_6": "float",
        "Vol_6": "float",
        "Ni_6F": "float",
        "Ni_6.1C": "float",
        "Ni_6.1C_max": "float",
        "Ni_6.1C_min": "float",
        "Ni_6.1T": "float",
        "Ni_6.1T_max": "float",
        "Ni_6.1T_min": "float",
        "FM_6.1_A": "float",
        "Ni_6.2C": "float",
        "Ni_6.2C_max": "float",
        "Ni_6.2C_min": "float",
        "Ni_6.2T": "float",
        "Ni_6.2T_max": "float",
        "Ni_6.2T_min": "float",
        "FM_6.2_A": "float",
        "Cu_resth": "float",
        "Ni_resth": "float",
        "Cu_1.1C": "float",
        "Ni_1.1C": "float",
        "Cu_1.2C": "float",
        "Ni_1.2C": "float",
        "Cu_2F": "float",
        "Ni_2F": "float",
        "Cu_2.1C": "float",
        "Ni_2.1C": "float",
        "Cu_2.2C": "float",
        "Ni_2.2C": "float",
        "Cu_3F": "float",
        "Ni_3F": "float",
        "Cu_3.1C": "float",
        "Ni_3.1C": "float",
        "Cu_3.2C": "float",
        "Ni_3.2C": "float",
        "Cu_2.1T": "float",
        "Ni_2.1T": "float",
        "Cu_2.2T": "float",
        "Ni_2.2T": "float",
        "Cu_3.1T": "float",
        "Ni_3.1T": "float",
        "Cu_3.2T": "float",
        "Ni_3.2T": "float",
        "Dens_3": "float",
        "Dens_1": "float",
        "Dens_2": "float",
        "Mass_3": "float",
        "FM_1.1_A": "float",
        "Cu_1.1C_max": "float",
        "Cu_1.1C_min": "float",
        "Ni_1.1C_max": "float",
        "Ni_1.1C_min": "float",
        "Ni_1.1T_max": "float",
        "Ni_1.1T_min": "float",
        "FM_1.2_A": "float",
        "Cu_1.2C_max": "float",
        "Cu_1.2C_min": "float",
        "Ni_1.2C_max": "float",
        "Ni_1.2C_min": "float",
        "Ni_1.2T_max": "float",
        "Ni_1.2T_min": "float",
        "FM_2.1_A": "float",
        "Cu_2.1C_max": "float",
        "Cu_2.1C_min": "float",
        "Cu_2.1T_max": "float",
        "Cu_2.1T_min": "float",
        "FM_2.2_A": "float",
        "Cu_2.2C_max": "float",
        "Cu_2.2C_min": "float",
        "Cu_2.2T_max": "float",
        "Cu_2.2T_min": "float",
        "FM_3.1_A": "float",
        "Cu_3.1C_max": "float",
        "Cu_3.1C_min": "float",
        "Ni_3.1C_max": "float",
        "Ni_3.1C_min": "float",
        "Cu_3.1T_max": "float",
        "Cu_3.1T_min": "float",
        "FM_3.2_A": "float",
        "Cu_3.2C_max": "float",
        "Cu_3.2C_min": "float",
        "Ni_3.2C_max": "float",
        "Ni_3.2C_min": "float",
        "Cu_3.2T_max": "float",
        "Cu_3.2T_min": "float",
        "Ni_rec": "float"
    }

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