from collections import namedtuple


Person = namedtuple('Person','x, y')
faisal = Person(x='Faisal',y=23)
print(faisal.x)
print(faisal._fields)
print(type(faisal))