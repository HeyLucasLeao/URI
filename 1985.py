def conv_inp():
    inp = input().split()
    inp = [int(x) for x in inp]
    return inp


def ped(array):
    card = {1001: 1.50,
            1002: 2.50,
            1003: 3.50,
            1004: 4.50,
            1005: 5.50}
    res = 0
    id_ped, qtd = array
    if id_ped in array:
        res += card[id_ped] * qtd
    return res


def qtd_ped(x = None):
    if x is None:
        x = int(input())
    res = 0
    for i in range(x):
        res += ped(conv_inp())
    return res


print(f"{qtd_ped():.2f}")