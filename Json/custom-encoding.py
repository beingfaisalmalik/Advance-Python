import json


def complex_encoding(z):
    if isinstance(z,complex):
        return {z.__class__.__name__: True, 'real':z.real, 'image': z.imag}
    else:
        raise TypeError('Josn is not serializable')
    
z = 5+9j

zsjon = json.dumps(z,default= complex_encoding)
print(zsjon)
print(type(zsjon))
