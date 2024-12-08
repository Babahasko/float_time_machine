import streamlit as st
from utils import show_colored_optimization

def show():
    st.title("Аналитика работы ML модели 🧠")
    if st.button("Показать изменения"):
        # Проверяем наличие данных в сессии
        if st.session_state['optimization_result'] is not None:
            # Подкрашиваем изменения
            st.write("Результаты оптимизации:")
            optimization_result_highlighted = show_colored_optimization(
                st.session_state["uploaded_file"],
                st.session_state['test_file'],
                st.session_state["optimization_result"])
            st.write('** - отметки для оптимизированных значений')
            st.write(optimization_result_highlighted)
            # Сохраняем данные в сессии
            st.session_state['highlight_optimization_result'] = optimization_result_highlighted
        else:
            st.info("Пожалуйста, Проведите оптимизацию перед показом изменений.")

    # Если данные имеются в сессии мы их отображаем
    if st.session_state['highlight_optimization_result'] is not None:
        if st.button("Показать отмеченные оптимизированные данные в текущей сессии"):
            st.write("Результаты оптимизации:")
            st.write(st.session_state['highlight_optimization_result'])
            st.write('** - отметки для оптимизированных значений')