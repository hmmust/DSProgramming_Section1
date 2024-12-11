import pandas as pd
import numpy as np
import datetime

t = datetime.datetime.today()
t2 = datetime.datetime(2024,10,15,8,0,0)
print(t2.strftime("%x")) #10/15/24
print(t2.strftime("%X")) #08:00:00
print(t2.strftime("%c")) #Tue Oct 15 08:00:00 2024
print(t2.strftime("%d/%m/%Y"))



