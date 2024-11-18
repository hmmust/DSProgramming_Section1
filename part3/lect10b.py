import pandas as pd
import numpy as np
data1 = [["Ahmad",21],["Zaid",20],["Leen",19],["Abdulrahman",20]]
data2 = np.array([[15,22],[20,23],[19,18],[16,17]])

df1 = pd.DataFrame(data1)
df1 = pd.DataFrame(data1,columns=["name","age"])
print(df1)
print(df1.age.value_counts())
df3 = pd.DataFrame(data2,columns=["first","second"])
df3['total'] = df3['first']+df3['second']
print(df3)

df1['total_mark'] = df3['total'] 
print(df1)
