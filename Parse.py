import pandas
import dateutil
import KN309Korzhov1

def parse(df):
# date/time parsing
    for i in range(df.shape[0]):
        df.loc[i, "day/month"] = dateutil.parser.parse(df.loc[i, "day/month"] + '2019').date()
        df.loc[i, "Time"] = dateutil.parser.parse(df.loc[i, "Time"])
    df['Time'] = pandas.to_datetime(df['Time'], format='%H:%M').dt.time
 # unit of measurement deletion
    for col in ['Humidity', 'Wind Speed', 'Wind Gust']:
        df[col] = df[col].replace('\D', '', regex=True).astype(int)
    df['Pressure'] = df['Pressure'].replace(',', '.', regex=True).astype(float)

    df.set_index('day/month', inplace=True)

data_to_parse = pandas.read_csv("DATABASE.csv", sep=';')

parse(data_to_parse)
KN309Korzhov1.display(data_to_parse)
