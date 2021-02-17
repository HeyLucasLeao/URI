from math import floor


dici = {'bonecos': 8,
        'arquitetos': 4,
        'musicos': 6,
        'desenhistas': 12}
atividade = {'bonecos': 0,
             'arquitetos': 0,
             'musicos': 0,
             'desenhistas': 0}


for _ in range(int(input())):
    _, grupo, hmhr = input().split()
    hmhr = int(hmhr)
    atividade[grupo] += hmhr

atividade = [floor(x/y) for x, y in zip(atividade.values(), dici.values())]

print(sum(atividade))
