def factorial(n):
    out = 1
    i = 1
    while i < n:
        i += 1
        out = out * i
    return out


x = factorial(3)
print(x)
