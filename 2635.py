procurados = set()
inp = []

for _ in range(int(input())):
    procurados.add(input())

for _ in range(int(input())):
    inp.append(input())

res = [[-1] for _ in range(len(inp))]

i = -1
for palavra in inp:
    count = 0
    tamanho = 0
    i += 1
    for chave in procurados:
        if palavra in chave[0:len(palavra)]:
            count += 1
            if len(chave) > tamanho:
                tamanho = len(chave)
            if inp.index(palavra) + 1 > len(res):
                res.append([count, tamanho])
            else:
                res[i] = [count, tamanho]

for list in res:
    print(*list)
