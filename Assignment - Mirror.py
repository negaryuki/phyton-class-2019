text = "Left -> -> -> -> Right -> -> -> "

mid = len(text) // 2

right = text[mid:]
left = text[:mid]

mirror_right = right[::-1]
mirror_left = left[::-1]

print(right, left)

print(mirror_right, right)
print(left, mirror_left)

