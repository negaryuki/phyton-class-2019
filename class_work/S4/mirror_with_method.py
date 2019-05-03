lst = ["L", "e", "f", "t", "->", "->", "->", "->", "R", "i", "g", "h", "t", "->", "->", "->"]

left = lambda lst: lst[:len(lst) // 2] + lst[:len(lst) // 2][::-1]
right = lambda lst: lst[len(lst) // 2:][::-1] + lst[len(lst) // 2:]


def new_left(lst):

