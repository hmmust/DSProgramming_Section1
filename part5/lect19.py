import json

mohammad = {"name":"Mohammad Ashor","age":21,"married":False}

students = [{"name":"Mohammad Ashor","age":21,"married":False},
            {"name":"Fuad Omari","age":20,"married":False}]

students2 = {"name":["Mohammad Ashor","Fuad Omari"],
             "age":[21,20],
             "married":[False,False]
            }

fh = open("./part5/students.json",mode="w")
json.dump(students,fh)
fh.close()
