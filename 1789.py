def corredores():
    num_inutil = int(input())
    testes = input().split(" ")
    testes = [int(x) for x in testes]
    Maior_vel = max(testes)
    if Maior_vel < 10:
        return 1
    if Maior_vel >= 10 and Maior_vel < 20:
        return 2
    if Maior_vel >= 20:
        return 3


while True:
    try:
        print(corredores())
    except EOFError:
        break
