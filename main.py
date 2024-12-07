import streamlit as st
import pandas as pd
import io

from utils import sort_columns
from utils import validate_data
from utils import custom_info
from utils import model_pipeline

# Настройка страницы
st.set_page_config(
    page_title="ML Модель",
    layout="wide")

# Заголовок
st.title("ML Модель: Загрузка таблицы значений за период времени")

# Создаем виджет для загрузки файла
uploaded_file = st.file_uploader("Выберите CSV файл", type="csv")

# Если файл был загружен
if uploaded_file is not None:
    # Читаем CSV файл в DataFrame
    df = pd.read_csv(uploaded_file)
    # df_sorted = sort_columns(df)

    #Проверка валидации данных и вывод сообщения пользователю
    message, color = validate_data(df)
    custom_info(message, color)

    # Выводим DataFrame на экран c сортировкой столбцов
    st.write("Содержимое CSV файла:")
    st.write(df)

    test = pd.read_csv('test.csv')
    result = model_pipeline(df, test)
    st.write("Содержимое оптимизированного файла:")
    st.write(result)

    # # Фильтрация данных
    # st.subheader("Фильтрация данных")
    # filter_column = st.selectbox("Выберите столбец для фильтрации", df.columns)
    # filter_value = st.text_input(f"Введите значение для фильтрации по столбцу '{filter_column}'")
    #
    # if filter_value:
    #     df_filtered = df[df[filter_column] == filter_value]
    #     st.write("Отфильтрованные данные:")
    #     st.write(df_filtered)
    #
    # # Сортировка данных
    # st.subheader("Сортировка данных")
    # sort_column = st.selectbox("Выберите столбец для сортировки", df.columns)
    # sort_order = st.selectbox("Выберите порядок сортировки", ["По возрастанию", "По убыванию"])
    #
    # if sort_order == "По возрастанию":
    #     df_sorted = df.sort_values(by=sort_column, ascending=True)
    # else:
    #     df_sorted = df.sort_values(by=sort_column, ascending=False)
    #
    # st.write("Отсортированные данные:")
    # st.write(df_sorted)
    #
    # # Сохранение данных
    # st.subheader("Сохранение данных")
    # output = io.StringIO()
    # df_sorted.to_csv(output, index=False)
    # csv_data = output.getvalue()
    #
    # st.download_button(
    #     label="Скачать отсортированные данные",
    #     data=csv_data,
    #     file_name="sorted_data.csv",
    #     mime="text/csv"
    # )
else:
    st.info("Пожалуйста, загрузите файл для формирования модели.")

# st.title("ML Модель: Загрузка тестового файла")
# uploaded_test_file = st.file_uploader("Выберите тестовый, который вы хотите улучшить") # , type="csv"

# test = pd.read_csv('test.csv')

# if uploaded_test_file is not None:
#     # Читаем CSV файл в DataFrame
#     test = pd.read_csv(uploaded_file)
#     # try:
#     #     test = pd.read_csv(uploaded_file, header = 0)
#     # except pd.errors.EmptyDataError:
#     #     test = pd.DataFrame(columns=pd.read_csv(uploaded_file, nrows=0).columns)
#     # df_sorted = sort_columns(df)
#
#     # Выводим формируемый test файл на основе разработанного алгоритма
# else:
#     st.info("Пожалуйста, загрузите тестовый файл для формирования оптимизации.")

# Применяем алгоритм к загруженным данным
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     result = model_pipeline(df, test)
#     st.write("Содержимое оптимизированного файла:")
#     st.write(result)


