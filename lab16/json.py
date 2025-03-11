import json

#1
#dict with student info
student_info = {
    "name" : "<NAME>",
    "age"  : 21,
    "courses" : ["Math", "Science", "History"]
}

#convert python dict to json string
json_string = json.dumps(student_info)
print("Serialized JSON string:", json_string)

#2

json_string = ''' 
{
    "name" : "<NAME>",
    "age"  : 21,
    "courses" : ["Math", "Science", "History"]
}
'''
student_info = json.loads(json_string)
print("Deserialized JSON string:", json_string)

#3
student_info = {
    "name" : "<NAME>",
    "age"  : 21,
    "courses" : ["Math", "Science", "History"]
}

filename = 'student.json'

with open(filename, 'w') as file:
    json.dump(student_info, file, indent=4)
print(f"Data has been written to {filename}")

with open(filename, 'r') as file:
    data_loaded = json.load(file)
    print("Data loaded from JSON file:", data_loaded)
