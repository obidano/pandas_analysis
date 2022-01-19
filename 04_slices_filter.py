import pandas as pd

df = pd.read_csv('./files/titanic.csv')

df.sex.describe()
df.sex.unique()
df.mean(numeric_only=True)

old_pass = df[df.age > 70]

# conditions
over_60 = df.age > 60
cabin_exists = df.cabin.notnull()

over_60_cabin_exists = over_60 | cabin_exists
over_60_cabin_exists = over_60 & cabin_exists

# null_df=df[df.cabin.isnull()]
not_null_df = df[df.cabin.notnull()]

df_over_60_cabin_exists=df[over_60_cabin_exists]
