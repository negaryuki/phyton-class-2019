country = {
    "Iran": "Tehran",
    "Germany": "Berlin",
    "England": "London"
}

phone = {
    "Model": "Iphone",
    "Country": "England",
    "Phone No.": 78798
}

# Method1: clear()

print(country)
country.clear()
print(country)
# _________________________________________________________________________
# Method2: copy()

phone2 = phone.copy()
print('phone2 = ', phone2)

# _________________________________________________________________________
# Method3: .fromkeys(keys, value)
new_dct = {}
val = 23
key = ('a', 'b', 'c')

new_dct = new_dct.fromkeys(key, val)
print(new_dct)
# _________________________________________________________________________
# Method4: .get()

get_key = phone.get("Model")
print(get_key)

# _________________________________________________________________________
# Method5: .items()
# change dic to tuple, and use indexes

phone_tpl = phone2.items()
phone2["Model"] = "Samsung"  #write the source
print(phone_tpl)



