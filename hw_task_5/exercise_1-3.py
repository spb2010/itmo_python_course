import pandas as pd
import numpy as np


def random_dataset():
    #1. Создайте DataFrame с рандомными целыми числами от 1 до 10, размером 10х10.
    df = pd.DataFrame(np.random.randint(0, 10, size=(10, 10)))
    return df


print(random_dataset())


def update_dataset(ds):
    # 2. В DataFrame из предыдущего задания добавьте индексы строк в виде латинских букв. Выведите на печать строку в которой все числа > 5, если такая есть
    df = ds
    df["indexes"] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    df = df.set_index("indexes")
    df = df[df.isin([6, 7, 8, 9]).any(axis=1)]
    return df


print(update_dataset(random_dataset()))


def random_dataset_tocsv():
    #3.	Создайте DataFrame с рандомными числами, размером 10х10.
    # a. добавьте индексы столбцов и строк в виде латинских букв
    df = pd.DataFrame(np.random.randint(0, 10, size=(10, 10)), index=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"])
    # b. Выведите на в консоль # i.	Размерность матрицы
    print("размерность матрицы:", df.shape)
    # ii.	индексы столбцов
    print("индексы столбцов:", df.columns.tolist())
    # iii.	среднее значение всех чисел матрицы
    print("#iii.среднее значение всех чисел матрицы:", df.mean(axis=0).sum(axis=0)/10)
    # iv.	запишите матрицу в csv
    df.to_csv("csv_file.csv")
    return df

print(random_dataset_tocsv())