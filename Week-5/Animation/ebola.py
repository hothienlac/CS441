import pandas as pd
import datetime


class Ebola():

    def __init__(self):
        ebola = pd.read_csv('ebola_data_db_format.csv')

        cases = ebola[ebola['Indicator'] == 'Cumulative number of confirmed Ebola cases']
        cases = cases.groupby('Date').sum().sort_index()
        cases['Date'] = cases.index
        cases['Date'] = cases['Date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').date())
        cases['Days'] = (cases['Date'] - cases['Date'].values[0]).apply(lambda x: x.days)
        cases = cases.rename(columns={'value': 'Case'}).drop('Date',axis=1)

        deaths = ebola[ebola['Indicator'] == 'Cumulative number of confirmed Ebola deaths']
        deaths = deaths.groupby('Date').sum().sort_index()
        deaths['Date'] = deaths.index
        deaths['Date'] = deaths['Date'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d').date())
        deaths['Days'] = (deaths['Date'] - deaths['Date'].values[0]).apply(lambda x: x.days)
        deaths = deaths.rename(columns={'value': 'Case'}).drop('Date',axis=1)

        data = {'Cases': cases, 'Deaths': deaths}
        self.__data = data

    def get_data(self):
        return self.__data

    def get_cases(self):
        return self.__data['Cases']