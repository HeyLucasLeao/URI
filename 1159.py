import functools as fn


def range_dez(x):
    return list(range(x, x + 10))


def list_apenas_pares(x):
    return list(filter(lambda x: x % 2 == 0, range_dez(x)))


def soma_pares(x):
    return fn.reduce(lambda a, b: a + b, list_apenas_pares(x))


def print_soma_pares():
    entrada = int(input())
    while entrada != 0:
        print(soma_pares(entrada))
        entrada = int(input())
