import numpy as np


def create_vector():
#1.	Создайте вектор размером 10 с рандомными значениями, отсортируйте и выведите в консоль.
    #для упрошения рандом от 0 до 10
    return(print(np.array(sorted(list(np.random.randint(1, 10, 10))))), int)


create_vector()

def chess_matrix():
#2.	Создайте матрицу 8х8 состоящую из 1 и 0 и заполненную в шахматном порядке
    zero_vector = np.zeros((8, 8))
    zero_vector[1::2, ::2] = 1
    zero_vector[::2, 1::2] = 1
    print(zero_vector)


chess_matrix()

def multiply_matrixes():
    #3.	Создайте матрицы 8x4 и 4x2 и перемножьте, результирующую матрицу выведите в консоль.
    a = np.random.randint(1, 10, (8, 4))
    b = np.random.randint(1, 10, (4, 2))
    return print(np.dot(a, b))


multiply_matrixes()


def vector_01():
    #4.Создать вектор размера 10 со значениями от 0 до 1, не включая ни то, ни другое.
    return print(np.random.random(10))


vector_01()

def matrix_generator(elements):
    #5. Создайте функцию, которая принимает число (количество элементов в матрице)
    elements_list = list()

    for i in range(1, int(elements / 2) + 1):
        # c. При проверке не учитывать матрицы с множителем “1”
        if elements % i == 0 and i != 1:
            elements_list.append(i)
    #e. если число нельзя разбить на множители без остатка выведите сообщение в консоль.
    if len(elements_list) == 0: return print("Нет множителей!")

    #b. Проверяет можно ли построить матрицы с размерностью из множителей принимаемого числа
    for i in range(0, len(elements_list)):
        for j in range(1, len(elements_list)):
            #d. постройте все возможные матрицы и выведите в консоль.
            print(np.random.randint(1, 10, (elements_list[i], elements_list[j])))


matrix_generator(12)
matrix_generator(5)
