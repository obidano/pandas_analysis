import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

pd.set_option('expand_frame_repr', False)

# stats descriptive
df = pd.read_csv('./files/winequalityN.csv')

# df.hist(column='alcohol')
# df.hist(column='alcohol', grid=False, bins=50, color='orange')
# sn.set_style('dark')
# sn.displot(df.alcohol, bins=35, kde=False, )
# df.alcohol.value_counts()
plt.plot(df.alcohol,)
plt.grid(True)
plt.title('RAPPORT ALCOOl')
plt.show()
