from matplotlib.dates import DayLocator, DateFormatter
import matplotlib.pyplot as plt
from numpy import array
from pandas import to_datetime
from collections import Counter

def display(df):
    print("Input the index(es) of graph(s) you want to display:")
    for i in range(1, len(df.columns)):
        print('|' + str(i) + '|' + ' - ' + str(df.columns[i]))
    input_cols = array(list(map(int, input().split())))

    for col in input_cols:
        if type(df.iloc[0, col]) is not str:
            x =  to_datetime(df.index.astype(str) + ' ' + df['Time'].astype(str))
            y = array(df.iloc[:, col])

            ax = plt.figure().add_subplot()
            ax.plot(x, y, label=df.columns[col])

            ax.xaxis.set_major_locator(DayLocator())
            ax.xaxis.set_major_formatter(DateFormatter('%m.%d'))

            plt.xlabel('Date')
            plt.ylabel(df.columns[col])

            ax.grid(which='major', color='black')
            ax.grid(which='minor', linestyle='dotted')
            ax.minorticks_on()

            plt.legend()
        else:
            dict = Counter(df.iloc[:, col])
            keys = array(list(dict.keys()))
            values = array(list(dict.values()))
            expl = [0.02] * len(values)

            fig, ax = plt.subplots()
            ax.pie(values, radius=1.25, explode=expl)

            plt.legend(labels=keys, bbox_to_anchor=(1.1, 1))

        plt.show()
