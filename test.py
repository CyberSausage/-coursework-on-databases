
f = {1: 2, 2: 3, 3: 4, 4: 8, 5: 1, 6: 5, 7: 7, 8: 6}
f_count = {1: 2, 2: 3, 3: 4, 4: 8, 5: 1, 6: 5, 7: 7, 8: 6}
f_new = {1: 2, 2: 3, 3: 4, 4: 8, 5: 1, 6: 5, 7: 7, 8: 6}

for i in range(1, 100):
    str_v = ""
    str_n = ""
    print(i+1)
    for l in range(1, len(f) + 1):
        f_new[l] = f[f_count[l]]
    for g in range(1, len(f) + 1):
        str_v += f"{g} "
        str_n += f"{f_new[g]} "
        f_count[g] = f_new[g]

    print(str_v)
    print(str_n)
