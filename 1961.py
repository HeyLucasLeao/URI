def set_sap():
    set_jog = input().split()
    cans = input().split()
    cans = [int(x) for x in cans]
    frog, qtd_can = set_jog
    return [int(frog), cans[:int(qtd_can)]]


def get_sap():
    frog, cans = set_sap()
    i = 0
    dif_c = cans[1:]
    for n in dif_c:
        if abs(cans[i] - n) > frog:
            return "GAME OVER"
        i += 1
    return "YOU WIN"


print(get_sap())
