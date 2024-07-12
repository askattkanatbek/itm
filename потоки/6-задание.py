import pandas as pd
import matplotlib.pyplot as plt

# Устанавливаем стиль 'ggplot' для графиков
plt.style.use('ggplot')
# Задаем размер фигуры для всех графиков
plt.rcParams['figure.figsize'] = (15, 5)

# Определяем переменную 'address', содержащую путь к текстовому файлу с данными
address = 'datasets/popularity-contest.txt'

try:
    # Читаем данные из файла, используя пробел в качестве разделителя, и исключаем последнюю строку ([:-1])
    popcon = pd.read_csv(address, sep=' ')
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit()

# Убедимся, что DataFrame не пуст
if popcon.empty:
    print("The DataFrame is empty.")
    exit()

# Печатаем первые пять строк DataFrame для предварительного просмотра
print("Initial data preview:")
print(popcon.head())

# Задаем названия столбцов для DataFrame
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']

# Печатаем столбцы и первые пять строк DataFrame для проверки
print("Columns set:")
print(popcon.columns)
print(popcon.head())

try:
    # Преобразуем значения в столбцах 'atime' и 'ctime' из строк в целые числа
    popcon['atime'] = popcon['atime'].astype(int)
    popcon['ctime'] = popcon['ctime'].astype(int)
except ValueError as e:
    print(f"Error converting columns to integers: {e}")
    exit()

try:
    # Преобразуем целочисленные значения в столбцах 'atime' и 'ctime' в формат даты и времени
    popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
    popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')
except Exception as e:
    print(f"Error converting columns to datetime: {e}")
    exit()

# Выводим тип данных столбца 'atime' и снова первые пять строк DataFrame
print("Data types after conversion:")
print(popcon.dtypes)
print(popcon.head())

# Фильтруем DataFrame, оставляя только те строки, где 'atime' больше 1 января 1970 года
popcon = popcon[popcon['atime'] > '1970-01-01']

# Создаем новый DataFrame 'nonlibraries', исключая строки, где в названии пакета содержится 'lib'
nonlibraries = popcon[~popcon['package-name'].str.contains('lib', na=False)]

# Сортируем 'nonlibraries' по убыванию времени создания ('ctime') и выводим первые 10 строк
print("Top 10 non-libraries packages sorted by creation time:")
print(nonlibraries.sort_values('ctime', ascending=False).head(10))
