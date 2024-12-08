import streamlit as st
import pandas as pd

from utils import validate_data
from utils import custom_info
from utils import model_pipeline
from utils import logger
from utils import show_colored_optimization

def show():
    # Инициализация переменных, в которых будут храниться данные сессии
    params = ['uploaded_file', 'test_file', 'optimization_result', 'highlight_optimization_result']
    for param in params:
        if param not in st.session_state:
            # Заполняем пустыми данными
            st.session_state[param] = None

    # Заголовок
    st.title("Загрузка обучающей выборки 🎓")

    # Создаем виджет для загрузки файла
    uploaded_file = st.file_uploader("Выберите CSV файл c обучающими данными", type="csv")

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

    # Если данные имеются в сессии мы их отображаем
    if st.session_state['uploaded_file'] is not None:
        if st.button("Показать выборку в текущей сессии"):
            st.write("Содержимое CSV файла:")
            st.write(st.session_state['uploaded_file'])

    else:
        st.info("Пожалуйста, загрузите файл для формирования модели.")


    st.title("Загрузка тестового файла 📝")
    uploaded_test_file = st.file_uploader("Выберите тестовый файл, который вы хотите улучшить", type="csv")

    # Если файл был загружен
    if uploaded_test_file is not None:
        test = pd.read_csv(uploaded_test_file)
        st.write(test)
        # Сохраняем данные в сессии
        st.session_state['test_file'] = test

    # Если данные имеются в сессии мы их отображаем
    if st.session_state['test_file'] is not None:
        if st.button("Показать тестовый файл в текущей сессии"):
            st.write("Содержимое тестового файла:")
            st.write(st.session_state['test_file'])
    else:
        st.info("Пожалуйста, загрузите тестовый файл.")

    # Заголовок
    st.title("Самая важная кнопка в этом приложении ⬇️")
    # Рисуем кнопку начала обработки
    if st.button("Начать оптимизацию!"):
        # Проверяем наличие данных в сессии
        if st.session_state['test_file'] is not None and st.session_state['uploaded_file'] is not None:
            # Применяем разработанную модель
            optimization_result = model_pipeline(st.session_state['uploaded_file'], st.session_state['test_file'])
            st.write('Результат оптимизации')
            st.write(optimization_result)
            st.session_state['optimization_result'] = optimization_result
        else:
            st.info("Пожалуйста, загрузите оба файла для их оптимизации.")

    # Если данные имеются в сессии мы их отображаем
    if st.session_state['optimization_result'] is not None:
        if st.button("Показать оптимизированные данные в текущей сессии"):
            st.write("Результаты оптимизации")
            st.write(st.session_state['optimization_result'])
    else:
        st.info("Пожалуйста, Загрузите обучающую и тестовую выборки")