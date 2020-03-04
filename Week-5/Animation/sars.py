import pandas as pd

class Sars:

    def __init__(self):
        data = pd.read_excel('./data/sars.xlsx', index_col=0)
        x = data['Date'].values[0]
        data['Days'] = data['Date'].apply(lambda a: (a-x).days)
        data = data[['Infected', 'Mortality', 'Days']]
        data = data.rename(columns={'Infected': 'Cases', 'Mortality': 'Deaths'})
        data = {'Cases': data[['Cases', 'Days']], 'Deaths': data[['Deaths', 'Days']]}
        self.__data = data

    def get_data(self):
        return self.__data

    def get_cases(self):
        return self.__data['Cases']

    def get_deaths(self):
        return self.__data['Deaths']