f = open("rosalind_hamm.txt")
file = f.read().split()
s = file[0]
t = file[1]
count = 0
for x in range(len(s)):
    if s[x] != t[x]:
        count += 1

print(count)