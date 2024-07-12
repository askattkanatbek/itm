# Импорт библиотеки pandas, matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from contextlib import contextmanager

# Устанавливаем стиль графиков 'ggplot'
plt.style.use('ggplot')
# Задаем размер для всех графиков
plt.rcParams['figure.figsize'] = (15, 5)

# Указываем путь к файлу CSV
address = 'datasets/bikes.csv'

@contextmanager
def open_csv(file_path, *args, **kwargs):
    try:
        df = pd.read_csv(file_path, *args, **kwargs)
        yield df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        yield None

# Используем контекстный менеджер для чтения файла
with open_csv(address, sep=',', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date') as fixed_df:
    if fixed_df is not None:
        # Выводим первые 3 строки DataFrame
        print(fixed_df.head(3))  # Можно также использовать fixed_df[:3]

        # Выводим первые 10 значений из столбца 'Berri 1'
        print(fixed_df['Berri 1'].head(10))

        # Строим график по данным из столбца 'Berri 1'
        fixed_df['Berri 1'].plot()

        # Добавляем подписи к осям и заголовок графика
        plt.xlabel('Дата')
        plt.ylabel('Количество')
        plt.title('График поездок на велосипеде по датам')

        # Отображаем график
        plt.show()  # Если указать block=True, программа будет ждать закрытия окна графика

        # Строим график по всем данным DataFrame
        fixed_df.plot(figsize=(17, 9))  # Изменяем размер окна графика
        plt.show()

        # Вычисляем сумму значений по столбцу 'Rachel1'
        column_sum = fixed_df['Rachel1'].sum()
        print(column_sum, 'сумма')
    else:
        print("Failed to load the DataFrame.")


