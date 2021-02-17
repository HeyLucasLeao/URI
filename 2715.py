from math import floor

while True:
    try:
        x = int(input())
        inp = []
        while len(inp) < x:
            inp.extend(input().split())
        inp = [int(x) for x in inp]
        mediana = floor(len(inp)/2) + 1
        rangel = inp[:mediana]
        gugu = inp[mediana:]
        total = sum(rangel) + sum(gugu)
        if sum(rangel)/total > sum(gugu)/total:
            gugu.append(rangel[len(rangel) - 1])
            rangel.pop(len(rangel) - 1)
        res = [sum(rangel), sum(gugu)]
        print(max(res) - min(res))
    except EOFError:
        break
