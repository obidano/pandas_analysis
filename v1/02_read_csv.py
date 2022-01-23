import pandas as pd

df = pd.read_csv('./files/pokemon.csv')

dupl = df[df.Type.duplicated()]
no_dupl = df[df.Type.duplicated() == False]

pokemon = df.Pokemon.sort_values(ascending=False)
# pokemon.get(10000)
# pokemon.get([0, 5])
# "Zubat" in pokemon.values
# pokemon.reset_index(drop=True)

df2 = df.set_index('Type')
types = df2['Pokemon']
# types.get('Grass')
# types.get([0, 5])
# types.get([0, 5, 119299292], default=0)

a=pd.read_csv('./files/ressources_humaines.txt',
              names=['nom', 'ville', 'cote','age','salaire', 'date'],
              sep=';')
a.date=pd.to_datetime(a.date)