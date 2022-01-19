import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('expand_frame_repr', False)

# df = pd.date_range(start='13/01/2019', end='14/07/2019', freq='H')
dfI = pd.date_range(start='2019/01/12', end='2019/02/14', freq='H')

#Now let's turn our series into a dataframe
df = pd.DataFrame(dfI, columns=['date'])

# And add a 'made up' column for sales data
df['sales'] = np.random.randint(0,1000,size=(len(df)))
df.set_index('date', inplace=True)

df.loc['2019-02']
df.loc['2019-02-03':"2019-02-10"]

daily_report=df.resample('D').sum()
# df.resample('T').sum()
df.resample('W').sum()
df.resample('M',kind='period').sum()
df.resample('Q',kind='period').sum()
df.resample('A',kind='period').sum()

# parse dates

df = pd.DataFrame({'year': [2015, 2016],
                   'month': [2, 3],
                   'day': [4, 5]})

df2=pd.to_datetime(df)
pd.to_datetime('20190101', format='%Y%m%d') 
pd.to_datetime('20190101', format='%Y%m%d', errors='ignore')
