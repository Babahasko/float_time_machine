import streamlit as st
import pickle
import numpy as np

# Загрузка обученной модели
# with open("model.pkl", "rb") as f:
#     model = pickle.load(f)

# Настройка страницы
st.set_page_config(
    page_title="ML Модель",
    layout="wide")

# Заголовок
st.title("ML Модель: Загрузка текста и предсказание")

# Загрузка файла
uploaded_file = st.file_uploader("Загрузите текстовый файл", type=["txt"])

if uploaded_file is not None:
    # Считывание содержимого файла
    text = uploaded_file.read().decode("utf-8")
    st.subheader("Содержимое файла:")
    st.text(text)

    # Обработка файла и работа с моделью
    if st.button("Сделать предсказание"):
        # Пример обработки текста: преобразуем текст в длину (или другое представление)
        input_data = np.array([[len(text.split())]])  # Например, количество слов
        # prediction = model.predict(input_data)
        st.success(f"Результат предсказания: {text}")
else:
    st.info("Пожалуйста, загрузите текстовый файл для анализа.")