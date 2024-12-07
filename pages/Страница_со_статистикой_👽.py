import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Аналитика работы ML модели")

# Пример данных
data = pd.DataFrame({
    "Feature 1": [1, 2, 3, 4, 5],
    "Feature 2": [10, 20, 30, 40, 50],
    "Prediction": [0, 1, 0, 1, 1]
})

st.subheader("Распределение данных")

# Гистограмма
fig, ax = plt.subplots(figsize=(10,6))
sns.histplot(data["Feature 1"], kde=True, ax=ax)
st.pyplot(fig)

st.subheader("Обзор данных")
st.dataframe(data)