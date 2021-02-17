import functools as fn


def sum(array):
    return f"{fn.reduce(lambda a, b: a + b, array):.1f}"


def media(array):
    return f"{fn.reduce(lambda a, b: a + b, array)/len(array):.1f}"


def operacao(inp, array):
    if inp == "S":
        return sum(array)
    if inp == "M":
        return media(array)


def matriz():
    array = []
    array_diagonal = []
    op = input()
    nest_list = []
    for i in range(12):
        for j in range(12):
            nest_list.append(float(input()))
            if j == 11:
                array.append(nest_list)
                nest_list = []
    for i in range(12):
        array_diagonal.extend(array[i][0:i])
    return operacao(op, array_diagonal)


try:
    print(matriz())
except:
    pass
