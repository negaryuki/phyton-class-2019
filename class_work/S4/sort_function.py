def sort(lst):
    lst_sorted = []
    lst_2 = lst.copy()

    while len(lst_2) > 0:
        mx = max(lst_2)
        lst_sorted.append(mx)
        lst_2.remove(mx)

    return lst_sorted


my_lst = [1, 2, 3, 4, 2, 1]

my_sorted_list = sort(my_lst)

print(my_lst)
print(my_sorted_list)

