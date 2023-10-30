from itertools import permutations

p_u = [2, 1, 5, 4, 3, 0, 0]
a = p_u.copy()
a.sort()
pur = permutations(a)
total_permutaions = list(pur)
print(total_permutaions)
try:
    index = 1+total_permutaions.index(tuple(p_u))
    print(f'The Index of' , index)
    print(f"The Next Permutation Is : {total_permutaions[index]}")
except IndexError:
    print(f"The Next Permutation Is : {total_permutaions[0]}")

