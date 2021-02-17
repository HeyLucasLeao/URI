def data():
    matriz = []
    i = 0
    x = int(input())
    qtd = int(x/3)
    res = []
    for _ in range(x):
        inp = input().split()
        inp[1] = int(inp[1])
        matriz.append(inp)
    matriz.sort()
    matriz.sort(key=lambda x: x[1], reverse=True)
    while i < qtd:
        res.append([i + 1, *matriz[i::qtd]])
        i += 1
    return res


res = data()

for x in res:
    print(f"Time {x[0]}")
    for duende in x[1:]:
        print(*duende, sep=" ")
    print()
