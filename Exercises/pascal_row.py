def factorial(n):
    out = 1
    i = 1
    while i < n:
        i += 1
        out = out * i
    return out


def combination(n, m):
    a = factorial(n)
    b = factorial(m) - factorial(n - m)
    res = a // b
    return res

