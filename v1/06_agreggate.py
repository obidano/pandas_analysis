import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('expand_frame_repr', False)

df = pd.read_csv('./files/amazon_fires.csv', encoding="ISO-8859-1")
states = df.estado.value_counts().shape
new_columns = {'ano': 'year',
               'estado': 'state',
               'mes': 'month',
               'numero': 'number_of_fires',
               'encontro': 'date'}
df.rename(columns=new_columns, inplace=True)

new_order = [4, 1, 0, 2, 3]
df = df[df.columns[new_order]]

df.number_of_fires.astype(str).str.isdigit().value_counts()

df.number_of_fires = df.number_of_fires.str.strip(' Fires').astype(float)

df2 = df.copy()
df2.dropna(inplace=True)
df2.reset_index(inplace=True, drop=True)
# translate months
month_translations = {'Janeiro': 'January',
                      'Fevereiro': 'February',
                      'Março': 'March',
                      'Abril': 'April',
                      'Maio': 'May',
                      'Junho': 'June',
                      'Julho': 'July',
                      'Agosto': 'August',
                      'Setembro': 'September',
                      'Outubro': 'October',
                      'Novembro': 'November',
                      'Dezembro': 'December'}

df2.month = df2.month.map(month_translations)

state_groups = df2.groupby('state')
rio = state_groups.get_group('Rio')
state_groups.size()
state_groups.sum()
state_groups['number_of_fires'].sum()
# state_groups.groups

# pivot
# pvt = df2.pivot_table(values='number_of_fires', index='state', aggfunc=np.mean)
pvt = df2.pivot_table(values='number_of_fires', index='state', aggfunc=np.mean, margins=True)
# state_groups['number_of_fires'].mean()
pvt_max = pvt['number_of_fires'].max() + 20  # aesthetic
# pvt.plot(kind='barh',xlim=(0, pvt_max), legend=False)
# plt.show()

df2['severity'] = np.random.randint(1, 5, df2.shape[0])
pvt2 = df2.pivot_table(values=['number_of_fires', 'severity'], index='state',
                       columns='year', aggfunc=np.size)

pvt3 = df2[df2.year> 2016].pivot_table(values=['severity'], index=['year','state'],
                       margins=True, aggfunc=[np.mean, np.min, np.max, np.sum])

# df2.groupby('state').get_group('Acre').set_index('year').loc[1998].describe()
# df2.groupby(['year','state']).count()['severity'].unstack().T.to_dict()
# df2.groupby(['state','year']).count()['severity'].unstack().to_dict()
# df2.groupby(['state','year']).count()['severity'].unstack().loc[:, 2019:2022].to_dict()
# df2.groupby('state')['number_of_fires'].agg(np.mean)
# df2.groupby('state')[['number_of_fires', 'severity']].agg(np.mean)
#df2.groupby('state')[['number_of_fires', 'severity']].agg([np.mean, np.max])
max_minus_min=lambda grouped_data: (grouped_data.max() - grouped_data.mean()) # std
grp_by=df2.groupby('state')['number_of_fires'].agg(max_minus_min)
# grp_by.reset_index()
# df2['number_of_fires'].plot(kind='kde')