"""
Write a python program to declare list of students
with their id, name, and first/second marks
then generate (using method) there email/total mark
"""
def generate_email_marks(stds):
    result=[]
    for s in stds:
        email=f"{s[0]}@uop.edu.jo"
        totalmark= s[2][0]+s[2][1]
        result.append([email,totalmark])
    return result
    
students = [(20201,"Fuad",[10,15]),
            (20202,"Zain",[12,13]),
            (20203,"Dana",[14,15])]

r = generate_email_marks(students)
print(r)