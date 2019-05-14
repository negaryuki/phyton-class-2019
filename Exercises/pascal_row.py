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


def pascal_row(n):
    row = []

    for i in range(n + 1):
        temp = combination(n, i)
        row = row + [temp]
        return row


def pascal(n):
    for i in range(n):
       print(pascal_row(i))


print(pascal(10))
