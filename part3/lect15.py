import pandas as pd
import numpy as np
from numpy import random
students = pd.read_csv("./part3/students.csv")
students_courses = pd.read_csv("./part3/students_courses.csv")
students['Year'] = students['Id'].astype(str).str[0:4].astype(np.int32)
students['Major']= students['Major'].str.strip()
students['Major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)
students['Id'] = students['Id'].astype(np.int16)

# Generate the highest GPA for each major and year
print(students.groupby(['Major'])[['GPA']].max())
print(students.groupby(['Major'])[['GPA']].agg('max'))

print(students.groupby(['Major','Year'])[['GPA']].agg('max'))

# Generate the average Age for each Year
print(students.groupby(['Year'])[['Age']].mean())





