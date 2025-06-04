n = 34
k = 2

def fib(n, k):
    if n > 2:
        res = fib(n-1, k) + fib(n-2, k)*k
        return res
    else:
        res = 1
        return res

print(fib(n, k))
