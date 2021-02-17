import functools as fn


def num_perfeito(x):
    array = []
    for n in range(1, x):
        if x % n == 0:
            array.append(n)
    if len(array) > 0 and fn.reduce(lambda a, b: a + b, array) == x:
        return f"{x} eh perfeito"
    else:
        return f"{x} nao eh perfeito"


def perguntar(entrada):
    i = 0
    while entrada > i:
        print(num_perfeito(int(input())))
        i += 1


perguntar(int(input()))
