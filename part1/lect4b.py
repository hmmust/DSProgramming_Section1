from collections import Counter

students = {'Khalid':2000,
            'Fuad':2004,
            'Raghad':2003,
            'Dana':2004
            }
students_ages = list( map( lambda s: 2024-s[1] ,students.items())  )
print(Counter(students_ages))

