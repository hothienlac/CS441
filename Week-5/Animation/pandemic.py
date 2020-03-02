import pandas as pd
import datetime

class Pandemic:

    def __init__(self):
        data = pd.read_csv('./data/pandemic.csv', encoding = "ISO-8859-1")
        data['Date'] = data['Update Time'].apply(lambda x:datetime.strptime(x, '%m/%d/%Y %H:%M').date())
        data = data.sort_values('Date', 0)
        x = data['Date'].values[0]
        data['Days'] = data['Date'].apply(lambda a: (a-x).days)
        data = data.replace({'Grand Total': 'Total'})
        data = data[data['Country'] == 'Total'][['Cases','Deaths','Days']].set_index('Days')
        data = {'Cases': data[['Cases', 'Days']], 'Deaths': data[['Deaths', 'Days']]}
        self.__data = data
    
    def get_data(self):
        return self.__data
