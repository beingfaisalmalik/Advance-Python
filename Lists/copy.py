#examle of Deep Copy 
print('Deep Copy')
lst = [1,2,3]
lst_new = lst
print(lst)
print(lst_new)

lst_new.append(1)
print(lst)
print(lst_new)


print('Shallow Copy')
#Example FO Shallow Copy Both Points To The Different Addresses In The Memory
lst = [1,2,3]
lst_new = lst.copy()
print(lst)
print(lst_new)

lst_new.append(1)
print(lst)
print(lst_new)