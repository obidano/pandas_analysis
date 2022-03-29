import numpy as np
import pandas as pdd
import swifter
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import dask.dataframe as pd

dtf_left = pdd.read_excel('./Classeur1.xlsx', 'T1 2016 CNSS RAWBANK')

dtf_right = pdd.read_excel('./Classeur1.xlsx', 'Overall prestataires')

chunksize = 500





# list_noms_l = dtf_left['NOMS'].to_list()
# list_noms_r = dtf_right['NOMS'].to_list()

# dtf_left['NOMS'] = '.*' + dtf_left['NOMS'] + '.*'

def merge_regex(df, df_dict, how, field):
    import re
    df_dict = df_dict.drop_duplicates()
    idx = [(i, j) for i, r in enumerate(df_dict[f'{field}']) for j, v in enumerate(df[f'{field}']) if re.match(r, v)]
    df_dict_idx, df_idx = zip(*idx)
    t = df_dict.iloc[list(df_dict_idx), 0].reset_index(drop=True)
    t1 = df.iloc[list(df_idx), df.columns.get_loc(f'{field}')].reset_index(drop=True)
    df_dict_translated = pd.concat([t, t1], axis=1)
    data = pd.merge(
        df,
        df_dict_translated,
        how=f'{how}',
        left_on=f'{field}',
        right_on=f'{field}'
    )
    data = data.drop_duplicates()
    return data

for chunk in np.array_split(dtf_left, len(dtf_left) // chunksize):
    # t += len(chunk)
    chunk['NOMS'] = '.*' + chunk['NOMS'] + '.*'
    a = merge_regex(dtf_right, chunk, 'inner', 'NOMS')
    break



