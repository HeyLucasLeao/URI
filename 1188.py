from typing import List


def operacao(inp: str, arr: List[int]):
    if inp == "S":
        return sum(arr)
    if inp == "M":
        return sum(arr)/len(arr)


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
    j = -2
    for i in range(7, 12):
        array_diagonal.extend(array[i][i+j:i])
        j -= 2
    return operacao(op, array_diagonal)


try:
    print(matriz())
except:
    pass
