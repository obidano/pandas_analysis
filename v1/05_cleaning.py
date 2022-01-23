import pandas as pd

df = pd.read_csv('./files/amazon_fires.csv', encoding = "ISO-8859-1")
states=df.estado.value_counts().shape
new_columns = {'ano' : 'year',
               'estado': 'state',
               'mes': 'month',
               'numero': 'number_of_fires',
               'encontro': 'date'}
df.rename(columns=new_columns, inplace=True)

new_order=[4, 1,0,2,3]
df=df[df.columns[new_order]]

df.number_of_fires.str.isnumeric()
df.number_of_fires.astype(str).str.isdigit()
df.number_of_fires.astype(str).str.isnumeric()
df.number_of_fires.astype(str).str.isdigit().value_counts()

# non numeriec
condit=~df.number_of_fires.astype(str).str.isnumeric()
df_non_numeric=df[condit]

# strip
df.number_of_fires=df.number_of_fires.str.strip(' Fires').astype(float)
# df.number_of_fires=df.number_of_fires.str.replace('', '0').astype(float)

df2=df.copy()
df2.isnull().sum()
df2.dropna(inplace=True)
df2.reset_index(inplace=True)
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

df2.month=df2.month.map(month_translations)
# df2.state=df2.state.str.title()
# df2.drop('date', axis=1).head()
# df2.drop(df2.index[0]).head()