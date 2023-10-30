from itertools import groupby

a = [1,2,3,4,5,6,7]
print(a)

def larger_then_3(value):
    return value>3
b=list(filter(larger_then_3, a))
print(b)

#using groupby 
group = groupby(a, key=larger_then_3)
print(group)

for key, value in group:
    print(key, list(value))
    

#using group by for even and odd filtering the data

def even(number):
    return number%2==0
    

even_odd_group = groupby(a, key=even)
for key,value in even_odd_group:
    print(key, list(value))
    
#group by age
persons = [{'name':'Faisal','age':21},{'name':'Ali','age':21},{'name':'Nasir','age':23},{'name':'Haleem','age':23}]
print(persons)


person_group = groupby(persons,key=lambda x:x['age'])
for key,value in person_group:
    print(key, list(value))
    