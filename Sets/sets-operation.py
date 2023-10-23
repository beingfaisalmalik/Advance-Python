st = {1,2,3,4,5,10}
print(st)
st2 = {1,2,3,4,5,6}
print(st2)
#union operation
#it will combine all the different element in the both sets and will return it
st3 = st.union(st2)
print(st3)

#will return a set that has element present in the st but not in the st2
st4 = st.difference(st2)
print(st4)

#returns a set that has both elements from set 1 set2

s5 = st.intersection(st2)
print(s5)


#returns true if there is no intersection of both sets
s6 = st.isdisjoint(st2)
print(s6)