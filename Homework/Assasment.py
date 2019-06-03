data = [50.3, 338.4, 626.6, 959.4, 1317.9, 1716.7, 2134.3, 2565.5, 3085.6, 3626.7]

#Part 1

def duration(input_lst):
    i = 0
    duration_lst = []
    while i + 1 != len(input_lst):
        due_par = data[i + 1] - data[i]
        duration_lst.append(due_par)
        i += 1
    return duration_lst


duration_of_lst = duration(data)
print(duration_of_lst)

