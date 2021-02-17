def set_dict():
    alu = {}
    loop = int(input())
    for i in range(loop):
        inp = input().split()
        a, b = inp
        b = float(b)
        alu[a] = b
    return alu


def t(par):
    max_v = 0
    for n in par:
        if par[n] > max_v:
            max_v = par[n]
            key = n
    return key if max_v >= 8 else f"Minimum note not reached"


print(t(set_dict()))


