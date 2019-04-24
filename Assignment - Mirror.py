print(' Imagine a Mirror, right in the middle of the below list: ')
text = "Left -> -> -> -> Right -> -> -> "
mid = len(text) // 2
right = text[mid:]
left = text[:mid]
print(right, left)
print("now let's see what this mirror does to the list:")
mirror_right = right[::-1]
mirror_left = left[::-1]

print('right side : ', mirror_right, right)
print('left side : ', left, mirror_left)
