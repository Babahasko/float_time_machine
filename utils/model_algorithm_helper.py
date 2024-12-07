import pandas as pd

def round_for_restrictions(test_predict):
    test_predict[['Ni_1.1C_min', 'Ni_1.1C_max', 'Cu_1.1C_min',
       'Cu_1.1C_max', 'Ni_1.2C_min', 'Ni_1.2C_max', 'Cu_1.2C_min',
       'Cu_1.2C_max']] = test_predict[['Ni_1.1C_min', 'Ni_1.1C_max', 'Cu_1.1C_min',
       'Cu_1.1C_max', 'Ni_1.2C_min', 'Ni_1.2C_max', 'Cu_1.2C_min',
       'Cu_1.2C_max']].round(1)
    test_predict[['Cu_2.1T_min', 'Cu_2.1T_max', 'Cu_2.2T_min',
           'Cu_2.2T_max','Ni_4.1T_min', 'Ni_4.1T_max','Ni_4.2T_min', 'Ni_4.2T_max', 'Ni_5.1T_min', 'Ni_5.1T_max', 'Ni_5.2T_min', 'Ni_5.2T_max',
             'Ni_6.1T_min', 'Ni_6.1T_max',   'Ni_6.2T_min', 'Ni_6.2T_max' ]] = test_predict[['Cu_2.1T_min', 'Cu_2.1T_max', 'Cu_2.2T_min',
           'Cu_2.2T_max','Ni_4.1T_min', 'Ni_4.1T_max','Ni_4.2T_min', 'Ni_4.2T_max', 'Ni_5.1T_min', 'Ni_5.1T_max', 'Ni_5.2T_min', 'Ni_5.2T_max',
             'Ni_6.1T_min', 'Ni_6.1T_max',   'Ni_6.2T_min', 'Ni_6.2T_max' ]].round(2)
    test_predict[['Cu_3.1T_min', 'Cu_3.1T_max', 'Cu_3.2T_min',
           'Cu_3.2T_max', 'Ni_4.1C_min',
           'Ni_4.1C_max', 'Ni_4.2C_min',
           'Ni_4.2C_max', 'Ni_5.1C_min',
           'Ni_5.1C_max', 'Ni_5.2C_min',
           'Ni_5.2C_max', 'Ni_6.1C_min',
           'Ni_6.1C_max', 'Ni_6.2C_min',
           'Ni_6.2C_max']] = test_predict[['Cu_3.1T_min', 'Cu_3.1T_max', 'Cu_3.2T_min',
           'Cu_3.2T_max', 'Ni_4.1C_min',
           'Ni_4.1C_max', 'Ni_4.2C_min',
           'Ni_4.2C_max', 'Ni_5.1C_min',
           'Ni_5.1C_max', 'Ni_5.2C_min',
           'Ni_5.2C_max', 'Ni_6.1C_min',
           'Ni_6.1C_max', 'Ni_6.2C_min',
           'Ni_6.2C_max']].applymap(lambda x: "{:.2f}".format(round(x / 0.05) * 0.05))
    return test_predict

def show_colored_optimization(df,test, optimized_df):
    df['MEAS_DT'] = pd.to_datetime(df['MEAS_DT'])
    test['MEAS_DT'] = pd.to_datetime(test['MEAS_DT'])
    optimized_df['MEAS_DT'] = pd.to_datetime(optimized_df['MEAS_DT'])

    # Исходные диапазоны
    original_df = df[df['MEAS_DT'].isin(test['MEAS_DT'])][test.columns.values]
    original_df.reset_index(drop=True, inplace=True)

    # Проверка на совпадение индексов и столбцов
    if not original_df.index.equals(optimized_df.index) or not original_df.columns.equals(optimized_df.columns):
        raise ValueError("Исходный и оптимизированный DataFrame должны иметь одинаковые индексы и столбцы.")

    # Создаем копию оптимизированного DataFrame для выделения изменений
    highlighted_df = optimized_df.copy()
    # Проходим по всем ячейкам и сравниваем значения
    for index in original_df.index:
        for column in original_df.columns:
            if optimized_df.at[index, column] != original_df.at[index, column]:
                # Если значения различаются, выделяем ячейку
                highlighted_df.at[index, column] = f"**{optimized_df.at[index, column]}**"
    return highlighted_df