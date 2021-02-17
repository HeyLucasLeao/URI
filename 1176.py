import functools as fn


def fibonacci():
    array = []
    entrada = int(input())
    i = 0
    if entrada > 60:
        raise Exception("valor acima de 60")
    while entrada >= i:
        if len(array) > 1:
            array.append(array[-1] + array[-2])
        else:
            array.append(i)
        i += 1
    return f"Fib({entrada}) = {array[entrada]}"


def entradas(inp):
    i = 0
    while inp > i:
        print(fibonacci())
        i += 1


entradas(int(input()))
