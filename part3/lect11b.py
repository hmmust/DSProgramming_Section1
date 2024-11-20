import pandas as pd
import numpy as np
data1 = {"name":["Ahmad","Zaid","Leen"],
         "age":[21,20,19]
         }
data2 = {"name":pd.Series(["Sara","Abdulrahman","Rama"]),
         "age":pd.Series([19,22,23]),
         }
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
df3= pd.concat([df1,df2])#,ignore_index=True)
df3=df3.reset_index(drop=True)
df3['birthyear'] = 2024-df3['age']
df3['rank'] = np.random.randint(100,999,len(df3))
#df3.pop('age')
del df3['age']
#df3=df3.drop(5)
#df3.drop(5,inplace=True)
df3.drop([3,5],inplace=True)
df3.reset_index(drop=True,inplace=True)
print(df3[0:2])

print(df3.loc[0:0,['birthyear','name']])
print(df3.iloc[0:1,1:2])
df3= df3.loc[:,['rank','birthyear','name']]
print(df3)