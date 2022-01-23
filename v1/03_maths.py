import pandas as pd

df = pd.read_csv('./files/google_stock_price.csv', squeeze=True)

c=df.count()