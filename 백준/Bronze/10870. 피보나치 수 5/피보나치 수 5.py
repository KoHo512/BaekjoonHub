n = int(input())

# fibo(n) = fibo(n - 1) + fibo(n - 2) (단, n >= 2)


def fibo(n):
    if n == 0 or n == 1:
        return n

    return fibo(n - 1) + fibo(n - 2)


print(fibo(n))
