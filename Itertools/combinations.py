from itertools import combinations,combinations_with_replacement
a = [1,2,3]
comb = combinations(a,2)
print(list(comb))
#apny sath bhi combination lega in the combinatinos
comb = combinations_with_replacement(a,2)
print(list(comb))

