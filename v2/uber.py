import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import os
import chart_studio.plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from calendar import day_name
from folium.plugins import HeatMap
import folium

files = os.listdir("./data/uber/")
files2 = list(filter(lambda x: x.endswith('14.csv'), files))

pd.set_option('expand_frame_repr', False)
df_or = pd.DataFrame()
for f in files2:
    path = f"./data/uber/{f}"
    temp_df = pd.read_csv(path, encoding='utf8')
    df_or = pd.concat([df_or, temp_df])

# "{:,}".format(df.shape[0])
df = df_or.copy()
df['dtime'] = pd.to_datetime(df['Date/Time'], format='%m/%d/%Y %H:%M:%S')
df.drop(['Date/Time'], axis=1, inplace=True)
df['days'] = df.dtime.dt.day_name()
df['date'] = df.dtime.dt.date
df['hour'] = df.dtime.dt.hour
df['month'] = df.dtime.dt.month
df['minute'] = df.dtime.dt.minute

df.days = pd.Categorical(df.days, categories=list(day_name), ordered=True)
days_report = df.days.value_counts()
days_report.sort_index(inplace=True)

# voir traffic par jour de la semaine
# px.bar(x=days_report.index, y=days_report.values).show()

# voir traffic par heure
# plt.hist(df.hour) # il y a pic vers 15h
# plt.show()

# voir traffic par heure et par mois
# plt.figure(figsize=(40, 20))
# for i, month in enumerate(df.month.unique()):
#     plt.subplot(3, 2, i+1)
#     df[df.month==month]['hour'].hist()
#


# hour_monthly=df.groupby(('month'))['hour'].count()
# trace1=go.Bar(x=hour_monthly.index, y=hour_monthly.values, name='Priority')


# analyse demande par latitude
# ax=sn.pointplot(x='hour', y='Lat', data=df)
# ax=sn.pointplot(x='hour', y='Lat', data=df, hue='days')

# base=df.groupby(['Base','month'])['Lon'].count().reset_index()
# sn.lineplot(x='month', y='Lon', data=base, hue='Base')

# heat map
df_out=df[df.days=='Sunday']
rush=df_out.groupby(['Lat','Lon'])['days'].count().reset_index()
rush.columns=['Lat', 'Long', 'Trips']
basemap=folium.Map()
HeatMap(rush, zoom=50, radius=15).add_to(basemap)
basemap.save('map.html')
"""
df['days']=df.dtime.dt.day_name()
a=df.groupby([ 'days',df.dtime.dt.date ])['Lon'].count()
a=a.reset_index().set_index('days')
a.unstack().fillna(0).plot(kind='bar', legend=False)


plt.figure(figsize=(30, 20))
for i, d in enumerate(df.days.unique()):
    plt.subplot(2, 4, i+1)
    df[df.days==d]['month'].hist()

sn.displot(df.days)
"""
