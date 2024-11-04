import numpy as np
all_marks = np.array([[10.5,12,14,16],
                    [11,15,17,13],
                    [13,16,15,19]])
#print(np.sum(all_marks[0,:]))
#print(all_marks[0:2,1:3])
arr1 = np.zeros(10)
arr1.fill(10)
print(arr1)
arr2 = np.zeros((3,2))
arr2.fill(5)
print(arr2)
arr3 = np.ones((3,2))
print(arr3)
arr4 = np.eye(5)
print(arr4)
print(arr4.astype("i"))  #or arr4.astype(int)
print(arr4.astype(bool))  

marks = np.array([10,12,14,16],dtype=float)
print(marks)

marks_str = np.array(["10","12","ab"])
#print(marks_str.astype(int)) #Error#