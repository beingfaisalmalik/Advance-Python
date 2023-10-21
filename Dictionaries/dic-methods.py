dic = {'Name':'Faisal', 'age':21}
print(dic)

#keys
names = ['Faisal','Ali','Nasir']

#values
ages = [23,22,21]
name_dic = dic.fromkeys(ages)
print(name_dic)




#for getting the value of the specified key
name  = dic.get('Name')
print(name)


#for updating the key's value
dic.update({'Name':'Ali'})
print(dic)


#for removing the entire key value pair from the dictionary
dd = dic.pop('Name')
print(dd)

print(dic)

#for removing the only last key value pair from the dictonary
dic.popitem()
print(dic)


dic = {'Name':'Faisal'}
name = dic.setdefault('Name','Ali')
print(name)
print(dic)