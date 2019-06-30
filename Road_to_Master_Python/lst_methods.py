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
# IMPORTANT POINT: The Difference between .append and . extend is that if you use :
# .append for 2 data, the data will be nested in the list : ['a', [1, 2]]
# .extend for 2 data, then the data will be added just normally to the list : ['a', 1, 2]

# _________________________________________________________________________
# Method6: index()

print(lst3.index('c'))

# _________________________________________________________________________
# Method7: list.insert(index, element)

lst2.insert(0, 'apple')
print(lst2)

# _________________________________________________________________________
# Method7: list.pop(index) -----> If no parameter is passed, the default index -1

print(lst2)
print(lst2.pop())  # = lst2.pop(-1)
print(lst2)
print(lst2.pop(0))
print(lst2)

# let's mix some methods :

print(lst3)
element = lst2.pop(0)
print(element)
lst3.append(element)
print(lst3)

# _________________________________________________________________________
# Method8: .remove()

print('lst2 =', '', lst2)
lst2.remove(5)
print('new lst2 =', '', lst2)

# _________________________________________________________________________
# Method9: .reverse() -----------> The reverse() function doesn't take any argument.

print('lst2 =', '', lst2)
lst2.reverse()
print('new lst2 =', '', lst2)
# _________________________________________________________________________
# Method10: .sort() ----------------> Key: ..... & reversed = True/False

lst4 = [2, 33, 67, 98, 99]
print('lst4 =', '', lst4)
lst4.sort()
print('new lst4 =', '', lst4)
lst4.sort(reverse=True)
print('new lst4 =', '', lst4)


