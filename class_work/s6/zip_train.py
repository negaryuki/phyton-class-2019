lst1 = [1, 2, 3, 4, 5]
lst2 = [10, 20, 30, 40, 50]


def my_zip(a, b):
    out = []

    for i in range(len(a)):
        tmp = (a[i], b[i])
        out.append(tmp)
    return out


res = my_zip(lst1, lst2)

print(res)
