def analyze_data(df):
    # Основные статистические характеристики
    summary = df.describe()

    # Медианы
    medians = df.median()

    # Минимальные значения
    mins = df.min()

    # Максимальные значения
    maxs = df.max()

    return summary, medians, mins, maxs