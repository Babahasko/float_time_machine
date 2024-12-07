import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib

#функция для отображения графиков в отдельном окне
matplotlib.use('TkAgg')

# === Примерные данные (их можно заменить на реальный источник данных) ===
time = ['2024-07-08 12:15', '2024-07-15 12:00']
categories = ['Ni Conc', 'Ni Tail']
data_input = {'Ni Conc': [2.5, 1.9], 'Ni Tail': [0.3, 0.2]}
data_output = {'Ni Conc': [1.5, 0.5], 'Ni Tail': [0.5, 0.2]}

# Дополнительный пример для других графиков
example_data = {
    "index": ["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01"],
    "Column_1": [10, 15, 20, 25],
    "Column_2": [5, 10, 15, 20],
}

# Подготовка данных
data_index = example_data["index"]
column_1 = example_data["Column_1"]
column_2 = example_data["Column_2"]

# Для тепловой карты
heatmap_data = pd.DataFrame(data_input, index=time)

# === Создаём общую фигуру с несколькими графиками ===
fig, axs = plt.subplots(3, 2, figsize=(14, 16))  # 3 ряда, 2 колонки

# 1. Линейный график
axs[0, 0].plot(time, data_input['Ni Conc'], marker='o', label='Ni Conc (Input)', color='blue')
axs[0, 0].plot(time, data_output['Ni Conc'], marker='x', label='Ni Conc (Output)', color='red')
axs[0, 0].set_title("Линейный график (Ni Conc)")
axs[0, 0].set_xlabel("Время")
axs[0, 0].set_ylabel("Значение")
axs[0, 0].legend()

# 2. Столбчатая диаграмма
bar_width = 0.35
x = range(len(categories))
axs[0, 1].bar(x, [data_input['Ni Conc'][0], data_input['Ni Tail'][0]], bar_width, label='Input', color='blue')
axs[0, 1].bar([p + bar_width for p in x], [data_output['Ni Conc'][0], data_output['Ni Tail'][0]], bar_width, label='Output', color='red')
axs[0, 1].set_xticks([p + bar_width / 2 for p in x])
axs[0, 1].set_xticklabels(categories)
axs[0, 1].set_title("Столбчатая диаграмма (Input vs Output)")
axs[0, 1].legend()

# 3. Тепловая карта
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", ax=axs[1, 0])
axs[1, 0].set_title("Тепловая карта (Ni Conc & Ni Tail)")

# 4. Точечный график
axs[1, 1].scatter(data_input['Ni Conc'], data_input['Ni Tail'], label='Input', c='blue', edgecolor='k')
axs[1, 1].scatter(data_output['Ni Conc'], data_output['Ni Tail'], label='Output', c='red', edgecolor='k', marker='x')
axs[1, 1].set_title("Точечный график")
axs[1, 1].set_xlabel("Ni Conc")
axs[1, 1].set_ylabel("Ni Tail")
axs[1, 1].legend()

# 5. Линейный график для дополнительных данных
axs[2, 0].plot(data_index, column_1, marker="o", label="Column_1", color="blue")
axs[2, 0].plot(data_index, column_2, marker="x", label="Column_2", color="green")
axs[2, 0].set_title("Линейный график (Column_1 и Column_2)")
axs[2, 0].set_xlabel("Дата")
axs[2, 0].set_ylabel("Значения")
axs[2, 0].legend()

# === Дополнительный график при необходимости (пустой пример) ===
axs[2, 1].text(0.5, 0.5, "Здесь может быть ваш график", fontsize=12, ha="center")
axs[2, 1].set_title("Пустой график")
axs[2, 1].axis("off")  # Убираем оси

# --- Отрисовать все графики ---
plt.tight_layout()
plt.show()