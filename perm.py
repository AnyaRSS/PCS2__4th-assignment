from itertools import permutations
from math import factorial
f = open('rosalind_perm.txt')
N = f.read()
n = int(N)
print(factorial(n))
perm = permutations(range(1,n+1)) 

for el in perm:
    permutation = ''
    for i in el:
        permutation = permutation + str(i) + ' '
    print(permutation)

f.close()