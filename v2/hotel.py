import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import os
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.express as px

df = pd.read_csv('./data/hotel_booking/hotel_bookings.csv')

# check null
df.isnull().any()
df.isnull().sum()
df.isnull().values.any()
df.fillna(0, inplace=True)

# convert to list of dict
# df.head().to_dict('records')

# clean data
filter = (df.children == 0) & (df.adults == 0) & (df.babies == 0)
df2 = df[~filter].copy()

filter_cancel = df2.is_canceled == 0
country_data = df2[filter_cancel]['country'].value_counts().reset_index()
country_data.columns = ['country', 'guests']

fig=px.choropleth(country_data, locations=country_data.country,
              color=country_data.guests,
              hover_name=country_data.country,
              title="Home countries of guests")
# fig.show

hotels=df.hotel.unique()
hotel1=df2[(df2.hotel==hotels[0]) & (df2.is_canceled==0)]
hotel2=df2[(df2.hotel==hotels[1]) & (df2.is_canceled==0)]


h_cn=hotel1.country.value_counts()
labels=h_cn[:10].index
val=h_cn[:10]
trace=go.Pie(labels=labels, values=val, hoverinfo='label+percent', textinfo='value')


resort_hotel=hotel1.groupby('arrival_date_month')['adr'].mean().reset_index()
city_hotel=hotel2.groupby('arrival_date_month')['adr'].mean().reset_index()
all_hotels=resort_hotel.merge(city_hotel, on="arrival_date_month")
all_hotels.columns=['month',"price_resort","price_city"]