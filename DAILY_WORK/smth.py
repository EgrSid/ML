lst = []
for n in range(1, 1000):
    n_bin = bin(n)[2:]
    n_bin += str(n_bin.count('1') % 2)
    n_bin += str(n_bin.count('1') % 2)

    res = int(n_bin, 2)
    if res > 85:
        lst.append(n)
print(min(lst))