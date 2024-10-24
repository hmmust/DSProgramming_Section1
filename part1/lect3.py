import random
students = ('Khalid','Fuad','Raghad','Dana')
students_lower = [s.lower() for s in students if s[0] in 'ABCDEF' ]
students_emails = [(f'{s.lower()}@uop.edu.jo',f'{s[0]}{random.randint(100,999)}') for s in students ]
print(students_emails)

students_emails_d = {s:(f'{s.lower()}@uop.edu.jo',f'{s[0]}{random.randint(100,999)}') for s in students }
print(students_emails_d)
print(students_emails_d['Khalid'])
