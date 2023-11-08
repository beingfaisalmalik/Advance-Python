import json


#for encoding 
def complex_encoding(z):
    if isinstance(z,complex):
        return {z.__class__.__name__: True, 'real':z.real, 'image': z.imag}
    else:
        raise TypeError('Josn is not serializable')
    
z = 5+9j

zsjon = json.dumps(z,default= complex_encoding)
print(zsjon)
print(type(zsjon))


#for decoding The Json File
zdic = json.loads(zsjon)
#it will convert into the dictionary of the file of it with it in the next of it we have to decide weather to visit it o not in the next time we have to shecdlue it for the better cause for doing it in the tadk ofr 
print(type(zdic))

zdecode = json.loads(zdic)
print(zdecode)
