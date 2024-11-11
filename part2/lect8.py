import numpy as np
marks = np.array([14,11,15,14,17,13,16,12,19])
"""for i in marks:
    print(i)

for i in marks2:
    print(np.max(i))
    """
marks2 = np.array([[14,11],[15,14],[17,13],[16,12]])
marks2.sort()
marks2= np.sort(marks2)
for i in np.nditer(marks2): #marks.reshape(-1)
    print(i)