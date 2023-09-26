import numpy as np
import re

class File_analisys_nlo:
    #6.Постройте класс для анализа файла с данными:
    def __init__(self):
        #a. У класса есть константа - путь к файлу при инициализации
        PATH = "nlo.csv"
        self.path = PATH

    def read_file(self):
    #d. Создайте метод для чтения файла - метод считывает массив из файла и сохраняет в атрибут класса.
        pass


    def coutry(self):
    #e. Создайте метод который возвращает страну в которой больше всего наблюдений.
        pass

    def mounth(self):
    #f. Создайте метод который возвращает месяц за который чаще всего появлялись объекты НЛО
        pass

ufo = File_analisys_nlo()
ufo.read_file()