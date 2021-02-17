dici = {'SALIDA': 1, 'VUELTA': -1, 'ABEND': 'break'}
res_turista = 0
res_direcao = 0


while True:
    inp = input().split()
    if len(inp) == 1:
        print(res_turista, res_direcao, sep="\n")
        break
    direcao, turista = inp
    turista = int(turista)
    res_direcao += dici[direcao]
    res_turista += dici[direcao]*turista
