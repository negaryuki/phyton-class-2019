lst = ["L", "e", "f", "t", "->", "->", "->", "->", "R", "i", "g", "h", "t", "->", "->", "->"]

mid = len(lst) // 2

right = lst[mid:]
left = lst[:mid]

mirror_right = lst[mid:-1]
print(mirror_right)
print(right, left)
