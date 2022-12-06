f = open("rosalind_lgis.txt", "r") 
n = int(f.readline().strip())
arr = []
for num in f.readline().strip().split(" "):
    arr.append(int(num))

l = [1]*n
inc = []

for i in range(n):
    inc.append([arr[i]])
    #print(inc)
    for j in range(i):
        if arr[j] < arr[i]:
            l[i] = max(l[i], l[j] + 1)
            if len(inc[i]) <= len(inc[j]):
                inc[i] = inc[j] + [arr[i]]
                #print(inc[i])

l_inc = max(l, inc[l.index(max(l))])

increasing = ''
for el in l_inc:
    increasing = increasing + str(el) + ' '
print(increasing)


dec = []

for i in range(n):
    dec.append([arr[i]])
    for j in range(i):
        if arr[j] > arr[i]:
            l[i] = max(l[i], l[j] + 1)
            if len(dec[i]) <= len(dec[j]):
                dec[i] = dec[j] + [arr[i]]

l_dec = max(l, dec[l.index(max(l))])

decreasing = ''
for el in l_dec:
    decreasing = decreasing + str(el) + ' '
print(decreasing)

f.close()