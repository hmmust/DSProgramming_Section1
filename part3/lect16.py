import pandas as pd
import numpy as np
from numpy import random

students = pd.read_csv("./part3/students.csv",
                       names=['id','name','major','age','year','gpa'],header=0,
                       dtype={'year':np.int16})

cd= pd.Categorical(["A","C","D","D","C"],["A","B","C","D"])
df = pd.DataFrame(cd)
print(df)
print(df[0].cat.categories)
print(df[0].cat.codes)
students['major'].replace({'DSS':'DS'," SE":"SE"},inplace=True)
students['major'] = pd.Categorical(students['major'])
print(students)
print(students['major'].cat.categories)


