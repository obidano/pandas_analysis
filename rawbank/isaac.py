import numpy as np
import pandas as pd
import swifter
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

dtf_left = pd.read_excel('./Classeur1.xlsx', 'T1 2016 CNSS RAWBANK')

dtf_right = pd.read_excel('./Classeur1.xlsx', 'Overall prestataires')

list_noms_l = dtf_left['NOMS'].to_list()
list_noms_r = dtf_right['NOMS'].to_list()


# process.extractOne("LUYEYE MANTETO", dtf_right['NOMS'], score_cutoff=80)
# process.extract("LUYEYE MANTETO", dtf_right['NOMS'].to_list(), limit = 10)

# dtf_left['name_from_df2'] = dtf_left['NOMS'].apply(lambda x: process.extractOne(x, dtf_right['NOMS'].to_list(),score_cutoff=80))
def findONe(x, b):
    a = process.extractOne(x, b, score_cutoff=80)
    return a[0] if a else None


def searchN(a, b):
    r = []
    for i in a:
        s = findONe(i, b)
        if s is None: continue
        r.append(dict(left=i, right=s))




# a = np.vectorize(findONe)
#
# [dtf_left.NOMS in n for n in list_noms]
