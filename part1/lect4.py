students = {'Khalid':2000,
            'Fuad':2004,
            'Raghad':2003,
            'Dana':2004
            }
"""for s in students.items():
    print(s)"""

students_ages = list( map( lambda s: 2024-s[1] ,students.items())  )
print(students_ages)

students_ages = dict( map( lambda s: (s[0], 2024-s[1]) ,students.items())  )
print(students_ages)

students_old =  dict( filter( lambda s: s[1] >= 21 ,students_ages.items())  )
print(students_old)

students_sorted = dict( reversed(sorted(students_ages.items(),key= lambda s: s[1])))
print(students_sorted)