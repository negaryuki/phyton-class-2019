seq = [1, 1]
members = 6

while len(seq) < members:
    new_member = seq[- 1] + seq[- 2]
    seq = seq + [new_member]
    print(seq)

