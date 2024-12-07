import pandas as pd
from sklearn.neighbors import NearestNeighbors
from .model_algorithm_helper import round_for_restrictions


def model_pipeline(df, test, k = 10):
    # Отбираем признаки
    X = df[['MEAS_DT', 'Cu_oreth', 'Ni_oreth', 'Ore_mass', 'Mass_1', 'Mass_2', 'Dens_4',
            'Mass_4', 'Vol_4', 'Cu_4F', 'Ni_4F', 'Ni_4.1C', 'Ni_4.1T', 'FM_4.1_A',
            'Ni_4.2C', 'Ni_4.2T', 'FM_4.2_A', 'Dens_5', 'Mass_5', 'Vol_5', 'Ni_5F',
            'Ni_5.1C', 'Ni_5.1T', 'FM_5.1_A', 'Ni_5.2C', 'Ni_5.2T', 'FM_5.2_A',
            'Dens_6', 'Mass_6', 'Vol_6', 'Ni_6F', 'Ni_6.1C', 'Ni_6.1T', 'FM_6.1_A',
            'Ni_6.2C', 'Ni_6.2T', 'FM_6.2_A', 'Cu_resth', 'Ni_resth', 'Cu_1.1C',
            'Ni_1.1C', 'Cu_1.2C', 'Ni_1.2C', 'Cu_2F', 'Ni_2F', 'Cu_2.1C', 'Ni_2.1C',
            'Cu_2.2C', 'Ni_2.2C', 'Cu_3F', 'Ni_3F', 'Cu_3.1C', 'Ni_3.1C', 'Cu_3.2C',
            'Ni_3.2C', 'Cu_2.1T', 'Ni_2.1T', 'Cu_2.2T', 'Ni_2.2T', 'Cu_3.1T',
            'Ni_3.1T', 'Cu_3.2T', 'Ni_3.2T', 'Dens_3', 'Dens_1', 'Dens_2', 'Mass_3',
            'FM_1.1_A', 'FM_1.2_A', 'FM_2.1_A', 'FM_2.2_A',
            'FM_3.1_A', 'FM_3.2_A', 'Ni_1.1C_min', 'Ni_1.1C_max', 'Cu_1.1C_min', 'Cu_1.1C_max',
            'Ni_1.2C_min', 'Ni_1.2C_max', 'Cu_1.2C_min', 'Cu_1.2C_max',
            'Cu_2.1T_min', 'Cu_2.1T_max', 'Cu_2.2T_min', 'Cu_2.2T_max',
            'Cu_3.1T_min', 'Cu_3.1T_max', 'Cu_3.2T_min', 'Cu_3.2T_max',
            'Ni_4.1T_min', 'Ni_4.1T_max', 'Ni_4.1C_min', 'Ni_4.1C_max',
            'Ni_4.2T_min', 'Ni_4.2T_max', 'Ni_4.2C_min', 'Ni_4.2C_max',
            'Ni_5.1T_min', 'Ni_5.1T_max', 'Ni_5.1C_min', 'Ni_5.1C_max',
            'Ni_5.2T_min', 'Ni_5.2T_max', 'Ni_5.2C_min', 'Ni_5.2C_max',
            'Ni_6.1T_min', 'Ni_6.1T_max', 'Ni_6.1C_min', 'Ni_6.1C_max',
            'Ni_6.2T_min', 'Ni_6.2T_max', 'Ni_6.2C_min', 'Ni_6.2C_max', 'Ni_rec']]

    # Преобразуем столбец MEAS_DT в тип datetime, если это ещё не сделано
    X['MEAS_DT'] = pd.to_datetime(X['MEAS_DT'])

    # Группируем данные по двум часам и берем первое значение в каждой группе
    X['2h_interval'] = X.groupby(pd.Grouper(key='MEAS_DT', freq='2H')).ngroup()

    # Сворачиваем по 2 часам берем среднее
    X_agreg = X.groupby('2h_interval').mean()

    # Отбор признаков для определения близости
    # А именно удаления диапазонов так как логики их сравнивать нет, наша цель их предсказать
    knn_features = X_agreg[['Cu_oreth', 'Ni_oreth', 'Ore_mass', 'Mass_1', 'Mass_2',
                            'Dens_4', 'Mass_4', 'Vol_4', 'Cu_4F', 'Ni_4F', 'Ni_4.1C',
                            'Ni_4.1T', 'FM_4.1_A', 'Ni_4.2C', 'Ni_4.2T', 'FM_4.2_A', 'Dens_5',
                            'Mass_5', 'Vol_5', 'Ni_5F', 'Ni_5.1C', 'Ni_5.1T', 'FM_5.1_A',
                            'Ni_5.2C', 'Ni_5.2T', 'FM_5.2_A', 'Dens_6', 'Mass_6', 'Vol_6',
                            'Ni_6F', 'Ni_6.1C', 'Ni_6.1T', 'FM_6.1_A', 'Ni_6.2C', 'Ni_6.2T',
                            'FM_6.2_A', 'Cu_resth', 'Ni_resth', 'Cu_1.1C', 'Ni_1.1C',
                            'Cu_1.2C', 'Ni_1.2C', 'Cu_2F', 'Ni_2F', 'Cu_2.1C', 'Ni_2.1C',
                            'Cu_2.2C', 'Ni_2.2C', 'Cu_3F', 'Ni_3F', 'Cu_3.1C', 'Ni_3.1C',
                            'Cu_3.2C', 'Ni_3.2C', 'Cu_2.1T', 'Ni_2.1T', 'Cu_2.2T', 'Ni_2.2T',
                            'Cu_3.1T', 'Ni_3.1T', 'Cu_3.2T', 'Ni_3.2T', 'Dens_3', 'Dens_1',
                            'Dens_2', 'Mass_3', 'FM_1.1_A', 'FM_1.2_A', 'FM_2.1_A', 'FM_2.2_A',
                            'FM_3.1_A', 'FM_3.2_A']]

    # Далее будет происходить заполнение отсутствующих значений нулями.
    # Для чего это было сделано: это было сделано для таких случаев когда в течении 2 часов по какому либо признаку не было информации.
    # Какая тут логика: агрегации с отсутвующими признаками будут отдаляться от полных агрегаций путем вычисления косинусной близости.
    knn_features.fillna(0, inplace=True)

    # Будем смотреть топ 5 наиболее похожих ситуаций
    # значение k можно регулировать
    knn_features_values = knn_features.values
    nbrs = NearestNeighbors(n_neighbors=k, metric='cosine')
    nbrs.fit(knn_features_values)

    # Вычислений топ близких индексов, а также дистанций
    distances, indices = nbrs.kneighbors(knn_features_values)

    # записываем названия колонок с диапазонами, которые нужно улучшить
    diap = test.drop('MEAS_DT', axis=1).columns

    # Что мы делаем далее: перебор нашего X_agred, проверяем возможности улучшения.
    # Если она есть-улучшаем путем замены, используя исторические данные.
    final = X_agreg.copy()
    for i in range(len(indices)):
        l = 0
        p = 0
        indices[i]
        distances[i]
        for b in range(len(indices[i])):
            actual = indices[i, 0]
            sravn = indices[i, b]
            # близость со сравниваемой строкой является числом от 0 до 1. 0 максимальная близость.
            # (1-(sravn_prox* n_features)- штраф который влияет на Ni_rec в зависимости от близости
            # Это означает, что для данных с большим количеством признаков схожесть будет более критичной, и штраф для схожих строк будет выше.
            sravn_prox = distances[i, b]
            Ni_rec_actual = X_agreg.iloc[actual]['Ni_rec']
            Ni_rec_sravn = X_agreg.iloc[sravn]['Ni_rec'] * (1 - (sravn_prox * knn_features.shape[1]))
            if (Ni_rec_sravn > Ni_rec_actual) and (Ni_rec_sravn > l):
                l = Ni_rec_sravn
                p = sravn

        if p != 0:
            for feature in diap:
                # Здесь заменяем значения в final, используя .iloc для позиционного индекса
                final.iloc[actual, final.columns.get_loc(feature)] = X_agreg.iloc[p, X_agreg.columns.get_loc(feature)]

    # Начинаем формирование теста

    # Создаем поля признаков для каждого временного диапазона
    testovaya = X[X['MEAS_DT'].isin(test['MEAS_DT'])]

    # Как и для X, делаем 2-ух часовую агрегацию
    test_agreg = testovaya.groupby('2h_interval').mean().reset_index()

    # заполняем данные для 2-ух часовых агрегаций для теста
    test_ag_predict = final[diap].loc[test_agreg['2h_interval'].values]

    # Оставим места для merge
    testovaya.drop(diap, axis=1, inplace=True)

    # разворачиваем наши диапазоны для теста
    df_test = pd.merge(testovaya, test_ag_predict, on=['2h_interval'], how='left')[test.columns.values]
    # Округления
    df_test = round_for_restrictions(df_test)
    # проверка
    if (df_test.shape[0] == test.shape[0]) and ((df_test.isna().sum().sum()) == 0):
        return df_test
    else:
        print('Ошибка в размерностях, возможно отсутствие данных в памяти')