import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Графики работы ML модели")

# Пример данных для визуализации
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Построение графика
fig, ax = plt.subplots()
ax.plot(x, y, label="Синусоида")
ax.set_title("Пример графика")
ax.legend()

# Отображение графика
st.pyplot(fig)

st.markdown("### Описание графика")
st.write("Здесь вы можете разместить описание графиков или результатов работы модели.")