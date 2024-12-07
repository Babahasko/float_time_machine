import streamlit as st
from utils import analyze_data

def show():
    st.title("Статистические данные обучающей выборки 📈")

    # Если данные имеются в сессии мы их отображаем
    if st.session_state['uploaded_file'] is not None:
        # Анализ данных
        summary, medians, mins, maxs = analyze_data(st.session_state['uploaded_file'])

        st.write("### Основные статистические характеристики")
        st.write(summary)

        st.write("### Медианы")
        st.write(medians)

        st.write("### Минимальные значения")
        st.write(mins)

        st.write("### Максимальные значения")
        st.write(maxs)

    else:
        st.info("Пожалуйста, загрузите файл для формирования статистических данных")