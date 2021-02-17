import functools


def entradas():
    qtd = int(input())
    while qtd > 0:
        senqImp()
        qtd -= 1


def map_int(number): return list(map(int, number))


def sort_and_int(array):
    input_int = map_int(array)
    input_int.sort()
    return input_int


def senqImp():
    input_string = input().split(" ")
    lista = sort_and_int(input_string)
    array = []
    i = lista[1]
    while i > lista[0]:
        if (i % 2 == 0 and i - 1 != lista[0]):
            array.append(i - 1)
        i -= 1
    if (len(array) == 0):
        array.append(0)
    return print(functools.reduce(lambda a, b: a + b, array))


entradas()
