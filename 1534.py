def matriz(x):
    array = []
    nested_list = []
    for i in range(x):
        nested_list.append([])
        for j in range(x):
            nested_list[i].append(3)
    array.extend(nested_list)
    return somar_interior(x, array)


def somar_interior(x, array):
    if len(array) > 1:
        j_d = 0
        i_d = x - 1
        for i in range(x):
            array[i][i] = 1
            array[i_d][j_d] = 2
            j_d += 1
            i_d -= 1
    return array


def print_mat(mat):
    for arr in mat:
        vet = list(map(lambda n: ("" + str(n))[-3:], arr))
        print(*vet, sep="")


def loop_print():
    while True:
        try:
            entrada = input()
        except EOFError:
            break
        else:
            print_mat(matriz((int(entrada))))


loop_print()
