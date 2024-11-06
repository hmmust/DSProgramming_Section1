import numpy as np
marks = np.array([10,12,14,16],dtype=float)
marks2 = np.array([11,14,17,20],dtype=float)
mark4 = marks.copy()
marks[0]= 15
print(marks,mark4)

mark5 = marks.view()
marks[0]= 20
print(marks,mark5)

print(mark4.base,mark5.base)

all_marks = np.array([[10.5,12,14,16],
                    [11,15,17,13],
                    [13,16,15,19]])


