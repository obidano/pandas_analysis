import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('expand_frame_repr', False)

df1 = pd.DataFrame({'item': ['A', 'B', 'C', 'D'],
                    'value': [1, 2, 3, 5]})

df2 = pd.DataFrame({'item': ['E', 'F', 'G', 'H'],
                    'value': [5, 6, 7, 8]})

df3 = pd.DataFrame({'item': ['E', 'F', 'G', 'H'],
                    'quanity': [2, 2, 1, 5]})

df4 = pd.DataFrame({'item': ['D', 'F', 'G', 'H'],
                    'quanity': [2, 2, 1, 5]})

df_concat = pd.concat([df1, df2])
df_concat_2 = pd.concat([df1, df3])  # different name columns
df_concat_3 = pd.concat([df1, df4])  # duplicate items
df_concat_3 = pd.concat([df1, df4], axis=1)

# append
df1 = pd.DataFrame({'item': ['A', 'B', 'C', 'D'],
                    'value': [1, 2, 3, 5]})

df2 = pd.DataFrame({'item': ['D', 'F', 'G', 'H'],
                    'quanity': [2, 2, 1, 5]})

df3 = pd.DataFrame({'item': ['I', 'J', 'K', 'L'],
                    'quanity': [3, 4, 7, 25]})

df_append = df1.append([df2, df3]).reset_index()
"""
Both join and merge can be used to combines two dataframes
 but the join method combines two dataframes on the basis of 
 their indexes whereas the merge method is more versatile and
 allows us to specify columns beside the index to join on for both dataframes.
"""


dfA = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

dfB = pd.DataFrame({'key': ['K5', 'K1', 'K2', 'K3'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})

dfA.join(dfB,lsuffix='_1')
dfA.merge(dfB, on='key')
dfA.merge(dfB, on='key',how='left')
dfA.merge(dfB, on='key',how='inner')