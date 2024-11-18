import pandas as pd
import numpy as np
data1 = ["Ahmad","Zaid","Leen","Abdulrahman"]
data2 = np.array([22,23,18,17,16])
data3 = {20201:22,
         20202:19,
         20203:21,
         20204:21
         }
ser1 = pd.Series(data1)
ser1 = pd.Series(data1,index=[20201,20202,20203,20204])
print(ser1)
ser2 = pd.Series(data2,index=[20201,20202,20203,20204,20205])
print(ser2)
ser3 = pd.Series(data3,dtype=float)
ser3 = ser3.astype(np.float32)
print(ser3)
print(ser3[20203])
print(ser3[[20202,20203]])
print(ser3[0:2])
print(ser3.iloc[0])
print(ser3[ser3>20])
print(ser3.where(ser3>20))

print("##",ser3.empty,ser3.size, ser3.axes,ser3.ndim)
print(ser3.head(n=2))
print(ser3.tail(n=2))
print(ser3.values)
print(ser3.index)
print(ser3.value_counts())