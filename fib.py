def fib(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1, k) + k*fib(n-2, k)
f = open("rosalind_fib.txt")
file = f.read().split()
n = int(file[0])
k = int(file[1])
print (fib(n,k))