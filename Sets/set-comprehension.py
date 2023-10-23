#set of even_numbers
st = {i for i in range(1,101) if i%2==0}
print(st)

l = [1,2,4,1,4,1]
unique_l = [*set(l)]
print(unique_l)