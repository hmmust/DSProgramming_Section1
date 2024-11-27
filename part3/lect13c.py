import pandas as pd
import numpy as np
from numpy import random
students = pd.read_csv("./part3/students.csv")

print(students[(students['Name'].str.startswith('A')) |  (students['Name'].str.startswith('B'))])
print(students[students['Name'].str[0].isin(["A","B"])])
print(students[students['Major'].isin(["CS"])])

