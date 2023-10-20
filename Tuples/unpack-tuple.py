t = tuple(i for i in range(0,3))
print(t)

one, two, three = t
print(one)
print(two)
print(three)

#UNPACKING USING THE ASTERIK
#asterik will return a list of unpacked numbers
one, three,*two = t
print(two)
print(three)

one, *q = t
print(one)