def matriz(x):
    array = []
    nested_list = []
    for i in range(x):
        nested_list.append([])
        for j in range(x):
            nested_list[i].append(0)
    array.extend(nested_list)
    return somar_interior(x, array)


def somar_interior(x, array):
    centro = int(x/2)
    for i in range(x):
        array[i][i] = 2  # diagonal esquerda
        array[-i][i-1] = 3  # diagonal direita
    for i in range(int(len(array)/3), x - int(len(array)/3)):
        for j in range(int(len(array)/3), x - int(len(array)/3)):
            array[i][j] = 1
    array[centro][centro] = 4  # centro
    return array


def print_mat(mat):
    for arr in mat:
        vet = list(map(lambda n: ("" + str(n))[-3:], arr))
        print(*vet, sep="")
    print()


while True:
    try:
        print_mat(matriz(int(input())))
    except EOFError:
        break
