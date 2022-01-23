import pandas as pd

data = ['Dan', "Sam", "Marc", "David", "Miller"]
# data = {'name': 'Dan', "age": 10, "date": 28}
data=[2.99, 4.45, 1.36]

ser = pd.Series(data)
val_arr = ser.values
multiply=ser.product()
