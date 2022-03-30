import numpy as np
import pandas as pd
import swifter
from rapidfuzz import process, utils as fuzz_utils

dtf_left = pd.read_excel('./Classeur1.xlsx', 'T1 2016 CNSS RAWBANK')

dtf_right = pd.read_excel('./Classeur1.xlsx', 'Overall prestataires')

df1 = dtf_left[['NOMS']].copy()
df2 = dtf_right[['NOMS']].copy()
s_mapping = {x: fuzz_utils.default_process(x) for x in df2.NOMS}

df1['indexx']=df1.index
a = df1.merge( df2, left_on="NOMS", right_on="NOMS", how='inner').set_index('indexx').drop_duplicates()
# df1.loc[df1.index.isin(a.index)].index
b = df1.set_index('indexx').drop(index=a.index)
a['correspondance'] = a['NOMS']


# dtf_left['NOMS'] = '.*' + dtf_left['NOMS'] + '.*'


def fuzzy_merge(df_1, s_mapping, key1, threshold=90, limit=1):
    df_x = df_1.copy()
    m1 = df_x[key1].apply(lambda x: process.extract(
        fuzz_utils.default_process(x), s_mapping, limit=limit, score_cutoff=threshold, processor=None
    ))
    df_x['correspondance'] = m1
    df_x['correspondance'] = df_x['correspondance'].apply(lambda x: '|'.join(i[0].upper() for i in x))
    # df_x = m1.copy()
    # print(m1.info())
    # print(df_x.info())
    # df_x.columns=['CompanyName','NOMS']
    # return df_x.head()
    # m2 = df_x['CompanyName'].apply(lambda x: ', '.join(i[2] for i in x))
    # df_x[key2] = m2

    return df_x


list_merged_df = []
chunksize = 1000
#
# for chunk in np.array_split(dtf_left, len(dtf_left) // chunksize):
#     # t += len(chunk)
#     # chunk['NOMS'] = '.*' + chunk['NOMS'] + '.*'
#     s_mapping = {x: fuzz_utils.default_process(x) for x in dtf_right.NOMS}
#     merged_df = fuzzy_merge(chunk[['NOMS']], s_mapping, 'NOMS', threshold=90)
#     list_merged_df.append(merged_df)
#     # break

# merged_df = fuzzy_merge(dtf_left[['NOMS']], dtf_right[['NOMS']], 'NOMS', 'NOMS', threshold=90)
merged_df = fuzzy_merge(b, s_mapping, 'NOMS', threshold=90)
c = pd.concat([a, merged_df])
# a=pd.concat(list_merged_df)
# c[c.CompanyName!='']
print('MATCH', c[c.correspondance != ''].shape)
c = pd.concat([a, merged_df])
