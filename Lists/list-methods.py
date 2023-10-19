fruits = ['Apple','Cherry','Mango','Date']
print(fruits)

#for adding element at the end
print('After Appending The Fruit')
fruits.append('Lemon')
print(fruits)


#for counting the occurences of the element in the list
print(fruits.count('Apple'))


#for removing the element based on the index
fruits.remove('Apple')
print(fruits)

#for removing the element based on the index from the list

fruits.pop(1)
#mango on the index 1 will be removed
print(fruits)

#for getting the index of the element from the list
print(fruits.index('Lemon'))

#for inserting the element based on the index
fruits.insert(1,'Pear')
#will be inserted at the 1 index before Date and after the Cherry
print(fruits)

#for adding another list of elements into the current list of fruits
fruits.extend(['Apple','Watermelon'])
print(fruits)

#for reversing the array based on first char of each element of the string
fruits.reverse()
print(fruits)

#for sorting the array based on the first element of the first char of the element of list
fruits.sort()
print(fruits)


# #for clearing the elements 
fruits.clear()
print(fruits)