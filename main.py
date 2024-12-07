import streamlit as st
import pandas as pd

from utils import validate_data
from utils import custom_info
from utils import model_pipeline
from utils import logger

# Настройка страницы
st.set_page_config(
    page_title="ML Модель",
    layout="wide")

# Инициализация переменных, в которых будут храниться данные сессии
params = ['uploaded_file', 'test_file']
for param in params:
    if param not in st.session_state:
        st.session_state[param] = 'Тут пока нет данных'

# Заголовок
st.title("ML Модель: Загрузка таблицы значений за период времени")

# Создаем виджет для загрузки файла
uploaded_file = st.file_uploader("Выберите CSV файл", type="csv")

# Если файл был загружен
if uploaded_file is not None:
    # Читаем CSV файл в DataFrame
    df = pd.read_csv(uploaded_file)

    #Проверка валидации данных и вывод сообщения пользователю
    message, color = validate_data(df)
    custom_info(message, color)

    # Выводим DataFrame на экран c сортировкой столбцов
    st.write("Содержимое CSV файла:")
    st.write(df)

    # Сохраняем данные в сессии
    st.session_state['uploaded_file'] = df

else:
    st.info("Пожалуйста, загрузите файл для формирования модели.")

st.title("ML Модель: Загрузка тестового файла")
uploaded_test_file = st.file_uploader("Выберите тестовый, который вы хотите улучшить", type="csv")

# Если файл был загружен
if uploaded_test_file is not None:
    test = pd.read_csv(uploaded_test_file)
    logger.info(f"{dir(test)}")
    st.write(test)
    # Сохраняем данные в сессии
    st.session_state['test_file'] = test

# Рисуем кнопку начала обработки
if st.button("Начать оптимизацию!"):
    # Проверяем наличие данных в сессии
    if 'test_file' in st.session_state and 'uploaded_file' in st.session_state:
        # Применяем разработанную модель
        optimization_result = model_pipeline(st.session_state['uploaded_file'], st.session_state['test_file'])
        st.write('Результат оптимизации')
        st.write(optimization_result)
    else:
        st.info("Пожалуйста, загрузите оба файла для их оптимизации.")



