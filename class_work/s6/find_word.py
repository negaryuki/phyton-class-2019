word = "been"
text = "half a bee, always a bee"

res = text.find("bee")

res_2 = text.find("bee", res + 2)
print(res)
print(res_2)
