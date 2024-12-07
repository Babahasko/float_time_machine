import streamlit as st

# Инициализация session_state, если его нет
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# Функция для отображения текущей страницы
def show_page():
    if st.session_state.page == 'main':
        import additional_pages.home as home
        home.show()
    elif st.session_state.page == 'analyze':
        import additional_pages.analyze as analyze
        analyze.show()
    elif st.session_state.page == 'statistic':
        import additional_pages.statistic as statistic
        statistic.show()

# Навигация
st.sidebar.title("Навигация")
if st.sidebar.button("📊 Загрузка данных"):
    st.session_state.page = 'main'
if st.sidebar.button("🔍 Анализ"):
    st.session_state.page = 'analyze'
if st.sidebar.button("📈 Статистические параметры"):
    st.session_state.page = 'statistic'

# Отображение текущей страницы
show_page()