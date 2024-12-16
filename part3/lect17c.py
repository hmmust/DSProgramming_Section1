import pandas as pd
import numpy as np
from sklearn.preprocessing import Binarizer,MinMaxScaler,StandardScaler,LabelEncoder,normalize


students = pd.read_csv("./part3/students.csv")
students['Major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)
encoder = LabelEncoder()
students['Major2']= encoder.fit_transform(students['Major'])
#print(encoder.classes_)
binarizer = Binarizer(threshold=3)
students['GPA_bin'] = binarizer.fit_transform(students.loc[:,['GPA']])
mm_scaler = MinMaxScaler(feature_range=(0,1))
students['GPA_mm'] = mm_scaler.fit_transform(students.loc[:,['GPA']])

print(students)

