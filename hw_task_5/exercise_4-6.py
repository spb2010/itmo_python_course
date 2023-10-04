import pandas as pd
import numpy as np
import myplotlib.pyplot as plt

def emoji_rating():
    emoji_ds = pd.read_csv("emojis.csv")
    #4.	Создайте DataFrame из файла emojis.csv.
    #a.	в столбце Rank указан рейтинг смайлов, отсортированный в порядке убывания частоты. (чем чаще использовался эмоджи тем ниже значение)
    #b.	Выведите в консоль самую популярную подкатегорию эмоджи
    return emoji_ds["Subcategory"][0]


print(emoji_rating())

def emoji_numbers():
    #5.	Создайте DataFrame из файла emojis.csv.
    emoji_ds = pd.read_csv("emojis.csv")
    #b.	Постройте график
    plt.plot(emoji_ds.groupby("Year")["Year"].count())
    plt.savefig("graph.jpg")
    # a.	Получите количество созданных эмоджи за каждый год
    return emoji_ds.groupby("Year")["Year"].count()


print(emoji_numbers())


def emoji_category(category):
    #6. Напишите функцию которая принимает строку - название категории
    emoji_ds = pd.read_csv("emojis.csv")
    # b. проверяет есть ли такая категория в наборе данных emojis.csv
    if emoji_ds[emoji_ds.Category == category]["Category"].count() > 0:
        # b. проверяет есть ли такая категория в наборе данных emojis.csv
        return print("Процент категорииб %:", emoji_ds[emoji_ds.Category == category]["Category"].count() / emoji_ds["Category"].count()*100)
        #c. возвращает сколько процентов эмоджи сделано по этой категории (пример: 10%). Или сообщение об отсутствии категории в наборе данных.
    else:
        return print("Нет такой категории!")

emoji_category("Smileys & Emotion")
emoji_category("Дгд")