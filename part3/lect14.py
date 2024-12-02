import pandas as pd
import numpy as np
from numpy import random
students = pd.read_csv("./part3/students.csv")
students_courses = pd.read_csv("./part3/students_courses.csv")
print(students.info())
print(students['Year'].isnull())
print(students[  students['Year'].isnull()  ])
d_student = students.dropna(axis=0) #axis=1
print(d_student)
#students['Year2'] = students['Year'].fillna(2020)
#students['Year3'] = students['Year'].fillna(students['Year'].median())
#students['Year4'] = students['Year'].fillna(method='pad')
#students['Year5'] = students['Year'].fillna(method='backfill')
#students['Year6'] = students['Id'].astype(str).str[0:4].astype(np.int32)
students['Year'] = students['Id'].astype(str).str[0:4].astype(np.int32)
students['Major']= students['Major'].str.strip()
students['Major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)
students['Id'] = students['Id'].astype(np.int16)
print(students.groupby(['Major']).groups)
print(students.groupby(['Major']).count())
print(students.groupby(['Major']).agg('count'))
print(students.groupby(['Major','Year']).agg('count'))
print(students.groupby(['Major','Year']).agg('mean'))





