# 2. Напишите программу - виртуальную модель процесса обучения.
# В программе должны быть объекты: ученик, учитель, учебные материалы.
# У каждого учителя должны быть атрибут:-    количество обученных учеников
# Для учителя добавьте метод “teach”: -    Метод принимает строку “название материала” и неизвестное количество учеников.
# Для каждого ученика вызывается метод “take” из класса ученика с параметром “название материала”.
# Атрибут учителя “количество обученных учеников” увеличивается на 1.
# У каждого ученика должен быть атрибут “knowledge” - список знаний.
# Для  ученика создайте метод “take” метод принимает строку знаний и добавляет ее в список знаний ученика.
# Класс учебных материалов - должен принимать любое количество не именованных атрибутов и при инициализации сохранять в один атрибут в виде списка.
# Для теста программы:
# - создайте объект по классу материалов. При инициализации передайте 5 строк:
# - “Python”
# - “Version Control Systems”
# - “Relational Databases”
# - “NoSQL databases”
# - “Message Brokers”
# - Создайте объект учителя
# - Создайте 4 объекта учеников
# - Проведите занятия по каждому материалу(5 раз вызовите метод teach) с произвольным набором учеников.
# - Выведите на печать знания каждого ученика.

# 3. Доработайте задачу 2
# а.Классы “ученик” и “учитель” должны быть наследованы от класса “человек”.
# i.У каждого человека должны быть атрибуты: ФИО, возраст, пол.
# b.Для классов “Материалы” и “Ученик” добавьте магический метод, для вызова функции len() от объектов классов.
# Материалы должны возвращать кол - во материалов, ученики кол - во знаний.
# c.добавьте в класс ученика, метод, позволяющий ученику случайно "забывать" какую - нибудь часть своих знаний.


class Person:
    # а.Классы “ученик” и “учитель” должны быть наследованы от класса “человек”.
    # i.У каждого человека должны быть атрибуты: ФИО, возраст, пол.
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Tutor(Person):
    # У каждого учителя должны быть атрибут:- количество обученных учеников
    # не дает передать атрибуты если они не поименованы, через *args и **kwargs нельзя, хотя судя по всему метод рабочий
    # https://ru.stackoverflow.com/questions/1195437/python-%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D1%83%D0%BF%D0%B5%D1%80-%D0%BA%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%BE%D1%80%D0%B0-%D0%9A%D0%B0%D0%BA-%D1%81%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C-%D1%82%D0%B0%D0%BA-%D1%87%D1%82%D0%BE%D0%B1%D1%8B-%D0%BF%D1%80%D0%B8-%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B8-%D1%8D%D0%BA
    # def __init__(self, student_number=0, *args, **kwargs):
    def __init__(self, name, age, sex, student_number=0):
        # super().__init__(*args, **kwargs)
        super().__init__(name, age, sex)
        self.student_number = student_number

    def teach(self, material_name, *args):
        # Для учителя добавьте метод “teach”: - Метод принимает строку “название материала” и неизвестное количество учеников.
        self.material_name = material_name
        self.args = args
        # Атрибут учителя “количество обученных учеников” увеличивается на 1.
        # self.student_number += len(args)
        for arguments in args:
            print(arguments)
            VictorLolov.take(material_name)
            self.arguments.take(material_name)


class Student(Person):
    # У каждого ученика должен быть атрибут “knowledge” - список знаний.
    def __init__(self, name, age, sex, knowledge: list = None):
        super().__init__(name, age, sex)
        self.knowledge = knowledge or []

    def take(self, knowledge_name):
        self.knowledge_name = knowledge_name
        self.knowledge.append(self.knowledge)


class materials:
    def __init__(self, *args):
        self.materials = args or []

    def __len__(self):
        return len(self.materials)


VictorIvanov = Tutor("Victor Ivanov", 50, "male")

# VictorIvanov.teach("Python", "VictorLolov", "SergeyZadikov", "ElenaSidorova")
# VictorIvanov.teach("Python", "Victor Lolov", "Sergey Zadikov", "Elena Sidorova")
# VictorIvanov.teach("Python", "Victor Lolov", "Sergey Zadikov", "Elena Sidorova")
# VictorIvanov.teach("Python", "Victor Lolov", "Sergey Zadikov", "Elena Sidorova")
# print(VictorIvanov.student_number)

ElenaSidorova = Student("Elena Sidorova", 20, "female")
VictorLolov = Student("Victor Lolov", 21, "male")
SergeyZadikov = Student("Sergey Zadikov", 19, "male")
ElenaSidorova.take("Python")
ElenaSidorova.take("Python1")
ElenaSidorova.take("Python2")
ElenaSidorova.take("Python3")
# print(ElenaSidorova.knowledge)
VictorIvanov.teach("Python", "VictorLolov", "SergeyZadikov", "ElenaSidorova")
