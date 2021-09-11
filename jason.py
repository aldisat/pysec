import json

#some JSON
x = '{ "name":"John", "age":30, "city":"New York" }'

#Parse x
y = json.loads(x)

#the result is a Python dictionary
print(y)

