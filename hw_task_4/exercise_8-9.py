import numpy as np
import re
from collections import Counter


class File_analisys_nlo:
    # 8.Постройте класс для анализа файла с данными:
    def __init__(self):
        # a. У класса есть константа - путь к файлу при инициализации
        PATH = "nlo.csv"
        self.path = PATH

    def read_file(self):
        # d. Создайте метод для чтения файла - метод считывает массив из файла и сохраняет в атрибут класса.
        with open(self.path) as file:
            self.words = file.readlines()

    def country(self):
        # e. Создайте метод который возвращает страну в которой больше всего наблюдений.
        countries = list()
        # сделаем список стран и в нем с помощью counter из collection
        for country in self.words:
            countries.append(country.split(",")[3])
        counted_numbers = Counter(countries)
        most_common_country = counted_numbers.most_common(1)[0][0]
        return print(most_common_country)

    def mounth(self):
        # f. Создайте метод который возвращает месяц за который чаще всего появлялись объекты НЛО
        # решаем анологично с предыдушей функцией
        months = list()
        # сделаем список месяцев и в нем с помощью counter из collection
        for month in self.words:
            months.append(re.split(r"/", month.split(",")[0])[0])
        counted_numbers = Counter(months)
        most_common_month = counted_numbers.most_common(1)[0][0]
        return print(most_common_month)

class File_analisys_ai:
#9.Постройте класс для анализа файла с данными:

    def __init__(self):
    # a. У класса есть константа - путь к файлу при инициализации
        PATH = "all_ai_tool.csv"
        self.path = PATH

    def read_file(self):
    # d. Создайте метод для чтения файла - метод считывает массив из файла и сохраняет в атрибут класса.
        with open(self.path) as file:
            self.words = file.readlines()

    def free_soft(self):
    # e.Создайте метод который возвращает ответ на вопрос - на какой тип инструмента платный или бесплатный чаще оставляют обзор (Review)
    # * Бесплатным считаем только полностью бесплатный инструмент (Free)
        free_with_review = list()
        not_free_with_review = list()
        for soft in self.words:
            if soft.split(",")[2] == "Free" and soft.split(",")[5] != "":
                free_with_review.append(soft.split(",")[0])
            elif soft.split(",")[2] != "Free" and soft.split(",")[5] != "":
                not_free_with_review.append(soft.split(",")[0])
        print(free_with_review)


    def useable_soft(self):
    # f.Создайте метод, который возвращает категорию задач (Useable For) для которой больше всего бесплатных инструментов
        pass

    def top_soft(self):
    #g.Создайте метод возвращающий топ 3 инструмента по запросу. Параметры запроса:
    #i.Платный или бесплатный - добавить возможность сортировки.
    #ii.задачи - (поиск искомой подстроки в результирующей строке)
    #iii.Основная категория - (поиск искомой подстроки в результирующей строке)
    #По умолчанию параметры необязательные и не должны влиять на выборку.
        pass


ufo = File_analisys_nlo()
ufo.read_file()
ufo.country()
ufo.mounth()

soft1 = File_analisys_ai()
soft1.read_file()
soft1.free_soft()