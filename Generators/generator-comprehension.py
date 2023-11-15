import sys
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator), "bytes")
print(next(mygenerator))
print(next(mygenerator))
# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist), "bytes")
print(mylist)