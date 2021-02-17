refeicoes = [int(x) for x in input().split()]
pedidos = [int(x) for x in input().split()]
res = [x - y for x, y in zip(refeicoes, pedidos)]
res = [x for x in res if x < 0]
print(sum(res)*-1)
