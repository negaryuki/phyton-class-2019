def sort(lst):
    lst_sorted = []

    while len(lst) > 0:
        mx = max(lst)
        lst.remove(mx)
        lst_sorted.append(mx)
        lst.remove(mx)

    return (lst_sorted)


my_lst = [1, 2, 3, 4, 2, 1]

my_sorted_list = sort(my_lst)

print(my_sorted_list)
