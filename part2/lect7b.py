import numpy as np
marks = np.array([10,12,14,16],dtype=float)
marks2 = np.array([11,14,17,20],dtype=float)
mark3 = np.concatenate((marks,marks2))
#print(mark3)

all_marks = np.array([[10.5,12],
                    [11,15],
                    [13,16]])
all_marks2 = np.array([[11.5,14],
                    [14,17],
                    [12,19]])
mark4 = np.concatenate((all_marks,all_marks2),axis=1)
#print(mark4)

mark5 = np.hstack((all_marks,all_marks2)) #vstack()
print(mark5.reshape(-1))
print(mark5.reshape(2,6))



