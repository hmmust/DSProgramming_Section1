import json

mohammad = {"name":"Mohammad Ashor","age":21,"married":False}

students = [{"name":"Mohammad Ashor","age":21,"married":False},
            {"name":"Fuad Omari","age":20,"married":False}]

students2 = {"name":["Mohammad Ashor","Fuad Omari"],
             "age":[21,20],
             "married":[False,False]
            }
mohammad_json = json.dumps(mohammad)
print(mohammad_json)
print(type(mohammad_json))
students_json = json.dumps(students)
print(students_json)
