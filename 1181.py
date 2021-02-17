import functools as fn


def sum(array):
    return f"{fn.reduce(lambda a, b: a + b, array):.1f}"


def media(array):
    return f"{fn.reduce(lambda a, b: a + b, array)/len(array):.1f}"


def linha_input():
    try:
        result = int(input())
        if result > 11 or result < 0:
            raise ValueError
    except ValueError:
        print(f"Linha inexistente de M[12][12]")
    else:
        return result


def operacao(inp, array):
    if inp == "S":
        return sum(array)
    if inp == "M":
        return media(array)


def matriz():
    linha = linha_input()
    op = input()
    nest_list = []
    array = []
    for i in range(0, 12):
        for j in range(0, 12):
            nest_list.append(float(input()))
            if j == 11:
                array.append(nest_list)
                nest_list = []
    return operacao(op, array[linha])


try:
    print(matriz())
except:
    pass
