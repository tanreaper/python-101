# 509. Fibonacci Number
from numpy import inf

def fib(n:int) -> int:
    f = [inf] *(n+1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]

print(fib(4))