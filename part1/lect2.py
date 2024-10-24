
students = ('Khalid','Fuad','Raghad','Dana')
"""print(type(students))
for s in students:
    print(s)
print(*students)
"""
std_iter= iter(students)
while True:
    try:
        print(next(std_iter))
    except StopIteration:
        break

for i in range(1,11,2):
    print(i)
    
for i in range(10,0,-1):
    print(i)

print([*range(10,0,-1)])