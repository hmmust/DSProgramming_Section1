import json

json_string = '[{"name": "Mohammad Ashor", "age": 21, "married": false}, {"name": "Fuad Omari", "age": 20, "married": false}]'
student_data = json.loads(json_string)
print(type(student_data))
print(student_data)