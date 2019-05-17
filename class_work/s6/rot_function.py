def rot_2(c):
    inps = 'fcjjm'
    indx = inps.index(c)
    outs = 'jmfcj'  # inps[-2:] + inps[:-2]#
    return outs[indx]


text = 'fcjjm'
for c in text:
    text += rot_2(c)
    print(text)