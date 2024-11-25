import pandas as pd
import numpy as np

students = pd.read_csv("./part3/students.csv")
#students=students.rename({"Year":"Entry_Year"},axis=1)

print(students[ students['GPA'] > 3 ])
print(students[ ~(students['GPA'] > 3) ])
print(students[ (students['GPA'] > 3) & (students['Age'] >20) ])
print(students.query(" GPA >3 and Age >20"))
print(students[ (students['Year'].isna())  ])
#print( students.loc[students['Year'].isna(),["Year"] ]) next lecture


#students['Entry_Year'] = students['Year'].astype(np.int16)
#print(students)
