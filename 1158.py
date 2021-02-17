import functools as fn


def soma_impar():
    dado = input().split(" ")
    x_dado = int(dado[0])
    y_dado = int(dado[1])
    array = []
    i_x = x_dado
    i_y = y_dado
    while i_y > 0:
        if (i_x % 2 != 0):
            array.append(i_x)
            i_y -= 1
        i_x += 1
    return fn.reduce(lambda a, b: a + b, array)


def entradas():
    i = int(input())
    while i > 0:
        print(soma_impar())
        i -= 1


entradas()
