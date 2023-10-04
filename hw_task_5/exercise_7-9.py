import pandas as pd
#import myplotlib.pyplot as plt


def data_analisys(data1, data2):
    #7. Напишите функцию которая принимает два параметра (диапазон дат)
    # b. Создайте DataFrame из файла BCT-USD.csv
    df = pd.read_csv("BCT-USD.csv").set_index("Date")
    # c. Строит графики по столбцам “Open” и “Close” за диапазон даты из параметров
    dff = df.loc[data1:data2, ["Open", "Close"]]
    print(dff)
    #plt.plot(dff)
    #plt.savefig("graph.jpg")

data_analisys("2022-01-21", "2022-01-25")


def volume_analisys():
    #Не решено
    #8. * Создайте DataFrame из файла BCT-USD.csv
    df = pd.read_csv("BCT-USD.csv")
    #df = df
    dff = pd.DatetimeIndex(df["Date"]).month
    #dff = df["Date"].dt.month
    print(dff)
    #a. выведите в консоль месяц за который был самый маленький объем (Volume)


volume_analisys()

def price_analisys():
    #Не решено
    #9. * Создайте DataFrame из файла BCT-USD.csv
    df = pd.read_csv("BCT-USD.csv")
    #a. Выведите в консоль месяцы за которые цена при закрытия в конце месяца была выше цены открытия на начало месяца
    #b. Если таких нет выведите соответствующее сообщение


price_analisys()