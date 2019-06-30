lst1 = [1, 2, 3, 4, 5, 'hi', 'ok', 'bye']
lst2 = ['a', 'b', 'c', 5, 6, 7]

# Method1: append()

lst1.append('appended')
print(lst1)

# _________________________________________________________________________
# Method2: clear()

lst1.clear()
print(lst1)

# _________________________________________________________________________
# Method3: copy()

lst3 = lst2.copy()
print(lst3)

# _________________________________________________________________________
# Method4: count()

lst3.append('a')
print(lst3)
print(lst3.count('a'))
# _________________________________________________________________________
# Method5: extend()

lst3.extend([1, 2])
print(lst3)
lst3.append([1, 2])
print(lst3)
#IMPORTANT POINT: The Difference between .append and . extend is that if you use :
# .append for 2 data, the data will be nested in the list : ['a', [1, 2]]
#.extend for 2 data, then the data will be added just normally to the list : ['a', 1, 2]

# _________________________________________________________________________
# Method6:
