import json

with open('Json/person.json','r') as f:
    person = json.load(f)
print(person)