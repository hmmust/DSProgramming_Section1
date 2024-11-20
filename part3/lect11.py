import pandas as pd
import numpy as np
data1 = [{"name":"Ahmad","age":21},{"name":"Zaid","age":20},{"name":"Leen","age":19}]
data2 = {"name":["Ahmad","Zaid","Leen"],
         "age":[21,20,19]
         }
data3 = {"name":pd.Series(["Sara","Abdulrahman","Rama"]),
         "age":pd.Series([19,22,23],dtype=float),
         "rank":np.random.randint(0,10,3)
         }
data4 = {"name":pd.Series(["Sara","Abdulrahman","Rama"],index=['a','b','c']),
         "age":pd.Series([19,22,23],dtype=float,index=['a','b','d']),
         }
df1 = pd.DataFrame(data1)
print(df1)
df2 = pd.DataFrame(data2)
print(df2)
df3 = pd.DataFrame(data3)
print(df3)
df4 = pd.DataFrame(data4,index=['a','b','c'])
print(df4)
