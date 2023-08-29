#Задача №1
def string_length(s = ''):
    #Напишите функцию которая возвращает длину принимаемой строки, по умолчанию строка пустая (s=’’). Пропишите все аннотации.
    return len(s)

print(string_length("lololo"))


#Задача №2
def bigger_length_list(list1, list2):
    #2)	напишите функцию которая
    #a)	принимает два списка
    #b)	возвращает длину самого длинного
    if len(list1) > len(list2):
        return len(list1)
    elif len(list1) < len(list2):
        return len(list2)
    else:
        return "Длина списков равна"

list1 = [1]
list2 = [1, 2]
print(bigger_length_list(list1, list2))


#Задача №3
def modify_list(input_list):
    #3)	Напишите функцию которая:
    #a)	принимает список с произвольными значениями
    #b)	добавляет к нему произвольное значение
    #c)	возвращает результирующий список
    input_list.append(4)
    return input_list

input_list = [1, 2, 3]
print(modify_list(input_list))


#Задача №4
def compare_to_100(digit):
    #4)	напишите функцию которая
    #a)	принимает число
    #b)	Если число больше 100 или меньше -100, то вывести в косоль символ “-”, иначе вывести на экран символ “+”
    if (digit > 100) or (digit < -100):
        return "-"
    else:
        return "+"


print(compare_to_100(101))
print(compare_to_100(-88))
print(compare_to_100(100))


#Задача №5
def contamination(string1, string2):
    #5)	Напишите функцию которая отвечает “ДА” или “НЕТ” на вопрос в комментарие

    if string1 in string2:
        return "Да"
    else:
        return "Нет"


print(contamination("test", "test1"))
print(contamination("tset", "test1"))

#Задача №6
def positive_sum(list1):
    #Функция на вход получает список, состоящий из 5 произвольных чисел. Найти количество положительных чисел среди них.
    sum = 0
    for elem in list1:
        if elem > 0:
            sum = sum + 1
    return sum


print(positive_sum([1, 1, 1, 1, 1]))
print(positive_sum([1, -1, -1, -1, -1]))
print(positive_sum([0, -1, -1, -1, -1]))


#Задача №7
def day_in_mouth(year1, mounth1):
    #7)	Функция на вход получает 2 переменные.
    #a)	Кол-во лет (int)
    #b)	Кол-во месяцев (int)
    #Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
    return (((year1) * 12) + mounth1) * 29


print(day_in_mouth(0, 2))
print(day_in_mouth(1, 2))


#Задача №8
def abreveature(string1: str):
    #Напишите функцию которая
    #на вход получает строковую переменную.
    #в строке содержится несколько слов
    #Возвращает строку состоящую из аббревиатур слов переменной.
    #Если на вход поступил другой тип данных, должно срабатывать исключение
    #Результат работы функции распечатайте в консоль

    try:
        words = string1.split()
    except:
        print("Неверный тип данных!")

    abreveature_word = ''

    for word in words:
        abreveature_word = abreveature_word + word[0]
    return abreveature_word

print(abreveature("ТЕОРИЯ РЕШЕНИЯ ИЗОБРЕТАТЕЛЬСКИХ ЗАДАЧ"))
print(abreveature(123))


#Задача №9
def factorio(digit):
    #Напишите функцию для нахождения факториала числа.
    #Факториал числа — это произведение всех целых чисел от 1 до искомого числа. К примере, факториал числа 6 равен 1*2*3*4*5*6 = 720.
    i = 1
    sum = 1
    while i < digit + 1:
        sum = sum * i
        i = i + 1
    return sum

print(factorio(4))
print(factorio(6))

#Задача №10
def multiply_list(lst):
    #10)	* Замените классическое представление цикла for в примере на любую конструкцию, так чтоб результат оставался тот же.
    i = 0
    while i < len(lst):
        lst[i] *= i
        i = i + 1
    return lst

lst = [2, 4, 5, 8, 9, 13]
print(multiply_list(lst))