def fibd(n, m):
    rabbits = [1, 1]
    for x in range(2, n):
        couples = rabbits[x - 1] + rabbits[x - 2]      #couples for month x
        if x == m:                                     #death in m months
            couples = couples - 1
        if x > m:
            couples = couples - rabbits[x - m - 1]
        rabbits.append(couples)
    return rabbits[-1]

f = open("rosalind_fibd.txt")
file = f.read().split()
n = int(file[0])
m = int(file[1])
print (fibd(n,m))