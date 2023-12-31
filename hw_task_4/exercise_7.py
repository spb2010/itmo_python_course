import numpy as np

def neuro(A: np.array, S: int, last = False):
    #7. напишите функцию которая принимает: вектор A длинной X, размер слоя S - натуральное число, Булевый параметр last - по умолчанию False
    # b.генерируется случайную матрицу B размером SxX
    B = np.random.randint(1, 10, (S, len(A)))
    print("lenA=", len(A))
    # c. создайте новую матрицу - произведение вектора A и матрицы B
    #C = np.dot(A, B)
    C = A*B
    D = np.array([])
    # d. Найдите сумму каждой строки результирующей матрицы - должен получится вектор размером S
    for matrix_row in C:
        D = np.append(D, np.sum(matrix_row))
    #e. Результирующий вектор проходит через функцию:
    if last == False:
        #i. Если last == False то функция - np.sin(x)
        D = np.sin(D)
    else:
        #ii. иначе np.maximum(x, 0)
        D = np.maximum(D, 0)

    #f. Вернуть результирующий массив и рандомную матрицу сгенерированную в начале функции
    return D, S


#g.Для теста вызовите функцию 3 раза:
#i.первый - длинна вектора 5, заполнен случайными числами. Размер слоя 10
A = np.array([1, 2, 3, 4, 5])
A, B = neuro(A, 10)
print(A) 
print(B)
#ii.второй - на вход передайте вектор из предыдущего запуска. Размер слоя 10
A, B = neuro(A, 10)
print(A)
print(B)
#iii.третий - на вход передайте вектор из второго запуска, размер слоя 5 и last = True.
#Значения результата переведите в проценты и выведите в консоль.
#D, B = neuro(A, S)
A, B = neuro(A, 5, True)
print(A)
print(B)

