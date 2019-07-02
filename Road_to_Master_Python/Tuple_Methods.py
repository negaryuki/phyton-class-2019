tpl = (1, 2, 3, 4, 1, 3, 3, 3, 1)

# Method 1 : count ()

print(tpl)
print(tpl.count(1))
print(tpl.count(3))

# _________________________________________________________________________
# Method2: index()

print(tpl)
print(tpl.index(2))
print(tpl.index(3))

# in this case, .index() will only define the first time '3' appeared in the tuple.
