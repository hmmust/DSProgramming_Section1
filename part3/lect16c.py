import pandas as pd
import numpy as np
import datetime

t = datetime.datetime.today()
t2 = datetime.datetime(2024,10,15,8,0,0)
t3 = datetime.datetime(2024,10,15,16,0,0)

ts = pd.date_range(t2, periods=5,freq='D')
ts = pd.date_range(t2, periods=5,freq='30min')
ts = pd.date_range(t2,t3, periods=10)


print(ts)



