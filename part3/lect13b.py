import pandas as pd
import numpy as np
from numpy import random
students = pd.read_csv("./part3/students.csv")
for i in students:
    print(i)
for i in students.itertuples():
    print(i.Name,i.Age)
    
print(type(students['Name']))
print(students['Name'].str[0:5])
print(students['Name'].str.lower().str.replace(' ','.')+"@uopstd.edu.jo")
students['Email']= students['Name'].str.lower().str.replace(' ','.')+"@uopstd.edu.jo"
students['Major'] = students['Major'].str.replace('DSS','DS')
print([f'{i.lower().replace(" ",'.')}@uop.edu.jo' for i in students['Name']])
students['Email2'] = [f'{i.lower().replace(" ",'.')}@uop.edu.jo' for i in students['Name']]
students['Password'] = [f'{i[0]}_{random.randint(100,999)}' for i in students['Name']]

print(students)
