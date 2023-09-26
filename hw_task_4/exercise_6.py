import numpy as np
import re

class File_analisys:
    #6.Постройте класс для анализа файла с данными:
    def __init__(self, path):
         #a.Класс принимает путь к файлу при инициализации
         self.path = path
         self.words = list()

    def file_read(self):
    # 6.b.Создайте метод для чтения файла - метод считывает массив из файла и сохраняет в атрибут класса.
    # Файл состоит из строк с произвольным текстом, элементами массива должны быть строки.
        with open(self.path) as file:
            self.words = file.readlines()

    def file_search(self, pattern):
    # c. Создайте метод поиска по тексту. Метод принимает паттерн поиска и возвращает список всех найденных совпадений.
        coincidences = list()
        for line in self.words:
            coincidence = re.findall(pattern, line)
            if coincidence:
                coincidences.extend(coincidence)
        return coincidences


test1 = File_analisys("test_text.txt")
test1.file_read()
print(test1.file_search("\w{3}"))