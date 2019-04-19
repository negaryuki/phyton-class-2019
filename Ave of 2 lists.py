num_List = [9, 23, 1, 2, 3, 4, 5, 6, 7, 8, 77, 9, 10, 11]
right_list = num_List[:8]
lenght_lists= len(num_List)//2

ave_right = max(right_list) / lenght_lists

left_list = num_List[8:]

ave_left = max(left_list) / lenght_lists

total = ave_left - ave_right

print("Total is", total)
