qtd, efetuados = [int(x) for x in input().split()]
inp = [[int(x) for x in input().split()] for _ in range(efetuados)]
inp = [sorted(x) for x in inp]
inp.sort()
etiquetas = set(range(1, qtd + 1))
ligacoes = set(inp[0])
for i in range(1, len(inp)):
    if any(x for x in ligacoes if x in inp[i]):
        ligacoes.add(inp[i][0])
        ligacoes.add(inp[i][1])
if ligacoes == etiquetas and len(ligacoes) > 1:
    print('COMPLETO')
else:
    print('INCOMPLETO')

