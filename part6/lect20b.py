import pandas as pd

df = pd.read_csv('./part6/students1.csv',chunksize=1)
print(df)