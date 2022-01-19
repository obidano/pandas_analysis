import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('expand_frame_repr', False)

df = pd.read_csv('./files/titanic.csv', encoding="ISO-8859-1")
# df2['number_of_fires'].plot(kind='kde')
# sibsp : number of sibings/spouse aboard
# parch: number of parents/child aboard

def get_family_size(sibsp,parch):
    family_size=sibsp+parch
    return family_size

def get_family_size_2(x):
    return x['sibsp']+ x['parch']

# df['family_size']=df[['sibsp','parch']].apply(lambda x: get_family_size(x['sibsp'], x['parch']), axis=1)
# df['family_size']=df[['sibsp','parch']].apply(lambda x: get_family_size_2(x), axis=1)
df['family_size1']=df['sibsp']+df['parch']

df['family_size']=df.apply(lambda x: get_family_size_2(x), axis=1)