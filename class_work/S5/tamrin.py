lst = [0.0, 1.5, 2.2, 2.8, 3.1, 9.2]
start = lst[:-1]
end = lst[1:]

lst_sorted =[]

for i in range(len(lst) - 1):
    difference = end[i] - start[i]
    lst_sorted.append(difference)



print(lst_sorted)
