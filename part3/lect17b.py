import pandas as pd
import numpy as np
import datetime

students = pd.read_csv("./part3/students.csv")

t = datetime.datetime(2024,12,16,8,0)
td2 = pd.Timedelta(minutes=15)
dr = pd.date_range(t,periods=len(students),freq=td2)
students['schedule'] = dr
td3 = pd.Timedelta(hours=1)
students['schedule'] = students['schedule'] + td3
print(students)
