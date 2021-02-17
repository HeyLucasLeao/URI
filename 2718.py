import re


def reparar():
    inp = int(input())
    txt = "".join(bin(inp))
    contar = re.findall('[1]+', txt)
    res = contar
    if len(res) > 0:
        res = len(max(contar))
    else:
        res = 0
    return res


[print(reparar()) for _ in range(int(input()))]
