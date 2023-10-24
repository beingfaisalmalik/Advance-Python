from collections import OrderedDict

d = OrderedDict()
d[1] = 'F'
print(d)

for key, value in d.items():
    print(key,value)
    
#in accordance with the python 3.7 or above dictonaries are ordered they rember ghe order in hich the element is inserted