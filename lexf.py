from itertools import product
f = open('rosalind_lexf.txt')
file = f.readlines()
let = list(map(str, file[0].split()))
n = int(file[1])
perm = list(product(let, repeat=n))
for el in perm:
    print(''.join(el), sep= '\n')