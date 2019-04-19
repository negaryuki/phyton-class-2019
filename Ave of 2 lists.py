num_List = [9, 23, 1, 2, 3, 4, 5, 6, 7, 8, 77, 9, 10, 11]
a_list = num_List[:8]

ave_right = max(a_list) / len(num_List)

left_list = num_List[8:]

ave_left = max(left_list) / len(num_List)

total = ave_left - ave_right

print("Total is", total)
