import pandas as pd
import numpy as np

students = pd.read_csv("./part3/students.csv")
print(students)
print(students.describe())
print(students.info())
print(students.columns)
print(students.dtypes)
print(students.head(2))
print(students.tail(2))

print(students['Year'].mean())
print(students.sum())
#print(students.mean()) # error 
students['gpa_rank']= students['GPA'].rank()
students['gpa_rank']= students['GPA'].rank(method="dense")
print(students)
print(students['GPA'].corr(students['Year']))
print(students['GPA'].cov(students['GPA']))





