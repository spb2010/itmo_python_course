import random
import time

#Задача 1
def word_elimination(input_string):
    #1.	Имеется строка состоящая из слов. Напишите функцию которая возвращает строку убрав из нее стоп слова.
    # Стоп слова находятся в списке:
    #a.	[“Python”, “php”, “go”, “C”]
    return print(" ".join(list((filter(lambda x: x not in ["Python", "php", "go", "C"], input_string.split())))))
    #не разобрался как мне перейти от фильтр объекта к строке без list и join


input_string = "pict Python php go C hjzkm"
word_elimination(input_string)


#Задача 2
def digits_sorting(input_digit, input_list = [2, 4, 7 , 3, 9]):
    #2.	Имеется список, состоящий из чисел.
    #Напишите функцию которая принимает число и возвращает список состоящий из элементов
    # первого списка кратных входному параметру.
    return print(list((filter(lambda x: x % input_digit == 0, input_list))))


digits_sorting(3)
digits_sorting(12)
digits_sorting(1)


#Задача 3
def cortage_return(*arg):
#3.	Напишите функцию, которая принимает любое количество не именованных аргументов
# и возвращает кортеж состоящий из аргументов у которых тип данных str
    return print(tuple(filter(lambda x: type(x) == str, arg)))


cortage_return(2, 'lol', 3.0, 'gogog')

#Задача 4
def intersection_set(list1 = [1, 2, 3, 4], list2 = [2, 4, 6, 8]):
#4.	Имеются два списка состоящие из произвольных элементов.
# Напишите функцию которая возвращает пересечение списков (элементы которые встречаются в и там и там)
    return print(set(list1) & set(list2))


intersection_set()


#Задача 5
def ladder(n):
#5.	Лесенка.
#Лесенкой - условный набор кубиков, в котором каждый последующий слой содержит меньше кубиков, чем предыдущий.
#Напишите функцию, вычисляющую число лесенок, которое можно построить из n кубиков.
#-	Длина каждой ступени может отличаться.
#-	n - натуральное число в диапазоне от 1 до 100.
    i = -1
    ii = 0
    ladder_level = 0
    #повторяем действие пока возможно поставить новые ступеньки (длина новой ступеньки меньше числа ставшихся кубиков)
    while i < n:
        #определяем длину ступеньки
        i = random.randint(ii, n)
        #уменьшаем общее число кубиков на i
        n = n - i
        ii = i
        ladder_level = ladder_level + 1
    return print(ladder_level)


ladder(10)
ladder(50)
ladder(100)

#Задача6
def integer_decorator(fn):
#6.	Напишите декоратор который выводит исключение в случае если декорируемая функция возвращает тип данных отличный от int
#Напишите 2 тестовые декорируемые функции с произвольными данными.
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if not isinstance(result, int):
            raise ValueError("Result type must be integer!")
        return result
    return wrapper

@integer_decorator
def integer_calculation(digit):
    return digit * 3

@integer_decorator
def integer_calculation2(digit):
    return digit ** 3

print(integer_calculation(3))
#print(integer_calculation("lol"))
print(integer_calculation2(3))
#print(integer_calculation2("lol"))

#Задача7
def repeate_if_exception(fn):
#7.	Напишите декоратор который запускает декорируемую функцию повторно,
# в случае если произошло исключение при первом запуске.
#Напишите 2 тестовые декорируемые функции с произвольными данными.
    def wrapper(*args, **kwargs):
        try:
            print("First Call!")
            return fn(*args, **kwargs)
        except ValueError:
            print("Second Call!")
            return fn(*args, **kwargs)
    return wrapper

@repeate_if_exception
@integer_decorator
def integer_calculation3(digit):
    return digit * 2

@repeate_if_exception
@integer_decorator
def integer_calculation4(digit):
    return digit ** 2

print(integer_calculation3(3))
#print(integer_calculation3("3"))
print(integer_calculation4(3))
#print(integer_calculation4("3"))


#Задача8
def list_sort(input_list):
#8.	* Пусть у нас есть список кортежей, которые описывают химические элементы (номер группы, порядковый номер, название)
#elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
#Отсортируйте список не учитывая при сортировке первый элемент каждого кортежа.
    return input_list.sort(key=lambda a: a[1])
    #почему то возвращает None, хотя вроде все норм


elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
print(list_sort(elements))




#Задача9
def time_calculation(fn):
    # 9.	* Напишите декоратор который измеряет время выполнения декорируемой функции.
    # Напишите 2 тестовые декорируемые функции с произвольными данными.
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        status, result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Время работы функции {result}: \t", end_time - start_time, " сек")
    return wrapper


@time_calculation
def calculation1():
    for i in range(6666):
        pass
    return True, print(calculation1)

@time_calculation
def calculation2():
    for i in range(66666):
        pass
    return True, print(calculation2)


calculation1()
calculation2()