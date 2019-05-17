word = "bee"
text = "half a bee, always a bee"


##res = text.find("bee")
##res_2 = text.find("bee", res + 2)
# print(res)
# print(res_2)

def find_all(text, word):
    ind = -1
    out = []
    while True:
        ind = text.find(word, ind + 1)
        if ind == -1:
            break
        out.append(ind)
    return out


finder = find_all(text, word)
print(finder)
