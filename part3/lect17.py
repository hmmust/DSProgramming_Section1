import pandas as pd
import numpy as np
import datetime

t = datetime.datetime.today()
t2 = datetime.datetime(2024,10,15,8,0,0)
t3 = datetime.datetime(2024,10,15,16,0,0)
print(type(t-t2))
td = pd.Timedelta(days=30,hours=10,minutes=30)
td2 = pd.Timedelta('10 hours')
print(t+td)
dr = pd.date_range(t,periods=5,freq=td2)
print(dr)

