import json

person = {'name':'faisal','age':21,'class':16,'hobbies':[1,2,3]}
person_json = json.dumps(person,indent=4,separators=(";" , "="),sort_keys=True)
print(person_json)
