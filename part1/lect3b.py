students = ('Khalid','Fuad','Raghad','Dana')

email_gen = lambda n: f'{n.replace(" ",".").lower()}@uop.edu.jo'
age_calc = lambda y: 2024-y

print(age_calc(2000))
print(email_gen("Khalid AbdelWahid"))

student_lower= map(lambda n: n.lower() ,students)
print(*student_lower)
