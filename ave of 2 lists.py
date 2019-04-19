num_list = [9, 23, 1, 2, 3, 4, 5, 6, 7, 8, 77, 9, 10, 11]

magic_number = len(num_list) // 2

print(magic_number)

right_list = num_list[:magic_number]
lenght_lists = len(num_list) // 2

ave_right = max(right_list) / lenght_lists

left_list = num_list[magic_number:]

ave_left = max(left_list) / lenght_lists

total = ave_left - ave_right

print("Total is", total)
