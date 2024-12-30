import json

fh= open("./part5/students.json",mode="r")
student_data = json.load(fh)
fh.close()

print(student_data['major'])
for n in student_data['name']:
    print(n)