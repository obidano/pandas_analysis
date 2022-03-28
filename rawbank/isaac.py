import numpy as np
import pandas as pd
import swifter
from sklearn import feature_extraction, metrics

dtf_left = pd.read_excel('./Classeur1.xlsx', 'T1 2016 CNSS RAWBANK')

dtf_right = pd.read_excel('./Classeur1.xlsx', 'Overall prestataires')
lst_b = dtf_left.NOMS.to_list()


# vectorizer = feature_extraction.text.CountVectorizer()
# X = vectorizer.fit_transform([a]+lst_b).toarray()
# lst_vectors = [vec for vec in X]
# cosine_sim = metrics.pairwise.cosine_similarity(lst_vectors)
# scores = cosine_sim[0][1:]
# match_scores = scores[scores >= threshold]
# match_idxs = [i for i in np.where(scores >= threshold)[0]]
# match_strings = [lst_b[i] for i in match_idxs]

def utils_string_matching(a, lst_b, threshold=None, top=None):
    vectorizer = feature_extraction.text.CountVectorizer()
    X = vectorizer.fit_transform([a] + lst_b).toarray()
    lst_vectors = [vec for vec in X]
    cosine_sim = metrics.pairwise.cosine_similarity(lst_vectors)
    scores = cosine_sim[0][1:]
    match_scores = scores if threshold is None else scores[
        scores >= threshold]
    match_idxs = range(len(match_scores)) \
        if threshold is None else [i for i in np.where(scores >= threshold)[0]]
    match_strings = [lst_b[i] for i in match_idxs]
    dtf_match = pd.DataFrame(match_scores, columns=[a],
                             index=match_strings)
    dtf_match = dtf_match[~dtf_match.index.duplicated(keep='first')] \
        .sort_values(a, ascending=False).head(top)
    return dtf_match


def vlookup(lst_left, lst_right, threshold=0.7, top=2):
    # try:
    dtf_matches = pd.DataFrame(columns=['string',
                                        'match', 'similarity'])
    list_b = lst_right.iloc[:, 0].tolist()
    for string in lst_left:
        a = lst_left.iloc[:, 0].tolist()[0]
        # print(a, list_b)
        # break
        dtf_match = utils_string_matching(a, list_b, threshold, top)
        dtf_match = dtf_match.reset_index().rename(columns=
                                                   {'index': 'match', string: 'similarity'})
        dtf_match["string"] = string
        dtf_matches = dtf_matches.append(dtf_match,
                                         ignore_index=True, sort=False)
    return dtf_matches[['string', 'match', 'similarity']]
    # except Exception as e:
    #     print("--- got error ---")
    #     print(e)


vlookup(dtf_left[['NOMS']], dtf_right[['NOMS']])
# a = dtf_left.NOMS.to_list()[0] # dtf_left.iloc[:, 0].tolist()[0]  # string
# lst_b =dtf_left.NOMS.to_list() # dtf_right.iloc[:, 0].tolist()  # list of strings
#
# vectorizer = feature_extraction.text.CountVectorizer()
# X = vectorizer.fit_transform([a]+lst_b).toarray()
# lst_vectors = [vec for vec in X]
# cosine_sim = metrics.pairwise.cosine_similarity(lst_vectors)
# scores = cosine_sim[0][1:]
# threshold = 0.7
# match_scores = scores[scores >= threshold]
# match_idxs = [i for i in np.where(scores >= threshold)[0]]
# match_strings = [lst_b[i] for i in match_idxs]
#
# top = 2
# dtf_match = pd.DataFrame(match_scores, columns=[a],
#                          index=match_strings)
# dtf_match = dtf_match[~dtf_match.index.duplicated(keep='first')
#                  ].sort_values(a, ascending=False).head(top)
# df1_nom = df[['NOMS']]
# df2_nom = df2[['NOMS']]


# inner_merged_total = pd.merge(df, df2, on=["NOMS", "NOMS"])
# def findNom(n):
#     a = np.where(df2_nom.NOMS.str.contains(n.NOMS, case=False), df2_nom.NOMS, np.nan)
#     b = a[~pd.isna(a)]
#     return b.item(0) if len(b) else np.nan
# return np.where(df2_nom.NOMS.contains.find(n), df2_nom.NOMS, np.nan).item(0)
# return df2_nom[df2_nom.NOMS.str.find(n).ge(0)]['NOMS']

# rhs = df.NOMS.apply(lambda x: df2[df2.NOMS.str.find(x).ge(0)]['NOMS']).bfill(axis=1).iloc[:, 0]
# rhs = df1_nom.NOMS.map(findNom)
# rhs = df1_nom.swifter.apply(findNom, axis=1)
