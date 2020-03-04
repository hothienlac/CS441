import pandas as pd
import datetime

class Corona:

    def __init__(self):
        data = pd.read_csv('./data/2019-nCoV-data.csv')
        data['Date'] = data['Date'].apply(lambda x:datetime.datetime.strptime(x, '%m/%d/%Y %H:%M').date())
        data = data.sort_values('Date', 0)
        x = data['Date'].values[0]
        data['Days'] = data['Date'].apply(lambda a: (a-x).days)
        data = data.groupby('Days')['Confirmed', 'Deaths', 'Recovered'].sum()
        data = data.rename(columns={'Confirmed': 'Cases'})
        data['Cases'] = data['Cases'].cumsum()
        data['Deaths'] = data['Deaths'].cumsum()
        data['Recovered'] = data['Recovered'].cumsum()
        data['Days'] = data.index
        data = {'Cases': data[['Cases', 'Days']], 'Deaths': data[['Deaths', 'Days']]}
        self.__data = data
    
    def get_data(self):
        return self.__data

    def get_cases(self):
        return self.__data['Cases']

    def get_deaths(self):
        return self.__data['Deaths']