s = set([1,2,3,4])
print(s)

#for adding the unique non existing element into the sets
s.add(11)
print(s)

#only accepts the iterable for adding the element
s.update([9,10])
print(s)

#reomves the last element and returns it
print(s.pop())
print(s)
print(s.remove(9))
print(s)

# remove raises the exception if element if not there its does not raise an exception if element is not in the list
print(s.discard)