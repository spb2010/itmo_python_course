import pandas as pd
import myplotlib.pyplot as plt


def data_analisys(data1, data2):
    #7. Напишите функцию которая принимает два параметра (диапазон дат)
    # b. Создайте DataFrame из файла BCT-USD.csv
    df = pd.read_csv("BCT-USD.csv").set_index("Date")
    # c. Строит графики по столбцам “Open” и “Close” за диапазон даты из параметров
    dff = df.loc[data1:data2, ["Open", "Close"]]
    print(dff)
    plt.plot(dff)
    plt.savefig("graph.jpg")

data_analisys("2022-01-21", "2022-01-25")


def volume_analisys():
    #Не решено
    #8. * Создайте DataFrame из файла BCT-USD.csv
    df = pd.read_csv("BCT-USD.csv")
    #a. выведите в консоль месяц за который был самый маленький объем (Volume)
    df['Date'] = pd.to_datetime(df['Date'])
    min_volume = df['Volume'].min()
    print(df['Date'][df['Volume'] == min_volume].dt.month_name().iloc[0])


volume_analisys()

def price_analisys():
    #Не решено
    #9. * Создайте DataFrame из файла BCT-USD.csv
    df = pd.read_csv("BCT-USD.csv")

    df['Date'] = pd.to_datetime(df['Date'])
    filtered_df = df[df['Close'] > df['Open']]
    df_months = filtered_df['Date'].dt.month_name().unique()
    #a. Выведите в консоль месяцы за которые цена при закрытия в конце месяца была выше цены открытия на начало месяца
    if len(df_months) > 0:
        print("Месяцы, в которых цена при закрытии была выше цены открытия:")
        for month in df_months:
            print(month)
    else:
        # b. Если таких нет выведите соответствующее сообщение
        print("Нет месяцев, в которых цена при закрытии была выше цены открытия.")


price_analisys()