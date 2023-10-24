from collections import Counter

a = 'aabbbccc'

# returns a dictionary with element as key and 
mu_counter = Counter(a)
print(a)
print(mu_counter)


# using the list as iterable
my_list = [0, 1, 0, 1, 2, 1, 1, 3, 2, 3, 2, 4]
my_counter = Counter(my_list)
print(my_counter)

#for element in the counter

print(list(my_counter.elements()))

