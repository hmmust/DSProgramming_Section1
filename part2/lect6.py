import numpy as np
marks = np.array([10.5,12,14,16])
print(marks)
print(marks.ndim)
print(marks.shape)
all_marks = np.array([[10.5,12,14,16],
                    [11,15,17,13],
                    [13,16,15,19]])
print(all_marks)
print(all_marks.ndim)
print(all_marks.shape)
print(all_marks[1,1])
print(np.mean(all_marks[:,1]))