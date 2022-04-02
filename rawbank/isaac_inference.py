import numpy as np
import pandas as pd
from rapidfuzz import process, utils as fuzz_utils

pd.set_option('expand_frame_repr', False)

# PARAMETRES VARIABLES
source_filename = './inference_2.xlsx'
resultat_filename = './inference_resultat_2.xlsx'

feuille_BASE1 = "BD1"
feuille_BASE2 = "BD2"

# TRAITEMENT
df1 = pd.read_excel(source_filename, feuille_BASE1)
df2 = pd.read_excel(source_filename, feuille_BASE2)
df1['montant_x'] = 0


def process_perfect_duplicate(x):
    a = df1[df1.PERSON == x]
    b = df2[df2.PERSON == x]
    if a.shape[0] == 0:
        return False
    if a.shape[0] == b.shape[0] and b.shape[0] > 1:
        return True
    return False


def sum_ens(x):
    return df2[df2.PERSON == x]['Montant 2'].sum()


df1['doublon_exacte'] = df1.PERSON.apply(process_perfect_duplicate)

df3 = df1[~df1.doublon_exacte].copy()
df3['montant_x'] = df3.PERSON.apply(sum_ens)

df4 = df1[df1.doublon_exacte].copy()[['PERSON', 'Montant 1']]
df4['indexx'] = df4.index
df5 = pd.merge(df4, df2, left_on='PERSON', right_on='PERSON')
df6 = df5[~(df5['Montant 1'] != df5['Montant 2'])].copy()
df6.rename(columns={"Montant 2": "montant_x"}, inplace=True)
df6.set_index('indexx', inplace=True)
dff = pd.concat([df3, df6])['montant_x']
df1.montant_x = dff
df1.drop(columns='doublon_exacte', inplace=True)
df1.to_excel(resultat_filename,index=False)
