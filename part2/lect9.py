import numpy as np
import numpy.random as rd

print(np.around((rd.rand()*100) +100,2))

print(rd.randint(10,20))
print(rd.randint(low=10,high=20))
print(rd.randint(low=10,high=20,size=(5)))
print(rd.randint(low=10,high=20,size=(5,5)))

print(rd.choice([10,20,30]))
print(rd.choice([10,20,30],size=5))
print(rd.choice([10,20,30],size=(5,5)))
#Given 5 employees in shop, generate 3-shifts schedule for 5 days
employees = np.array(["Ahmad","Qais","Rama","Lina","Zaid"])
shifts = rd.choice(employees,size=(5,3),p=[0.1,0.4,0.2,0.1,0.2])
rd.shuffle(shifts)
print(shifts)
#print(rd.permutation(shifts))