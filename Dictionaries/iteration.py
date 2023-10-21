dic = dict(Names=['Faisal','Ali','Nasir'],Ages=[12,12,32])

#looping on the all items

for key, values in dic.items():
    for items in values:
        print(items)
        
#for looping on the keys only 
for key in dic.keys():
    print(key)
    
#for looping on the values of the dictionaries
for value in dic.values():
    print(value)
    
    
