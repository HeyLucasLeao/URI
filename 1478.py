def matriz(x):
    array = []
    nested_list = []
    for i in range(x):
        nested_list.append([])
        for j in range(x):
            nested_list[i].append(1)
    array.extend(nested_list)
    return somar_interior(x, array)


def somar_interior(x, array):
    if len(array) > 1:
        k = 1
        y = x
        for i in range(1, x):  # faz primeira linha e coluna
            array[0][i] += k
            array[i][0] += k
            array[-1][i] = (array[-1][i] - y)*-1  # faz a última linha
            k += 1
            y -= 1
        for i in range(1, x-1):  # faz interna descrente
            y = array[0][i] - 2
            for j in range(1, x):
                array[i][j] += y
                y -= 1
        y = 2
        for i in range(1, x-1):  # faz interna crescente
            y = 2
            for j in range(1, x):
                if array[i][j] <= 0:
                    array[i][j] = y
                    y += 1
    return array


def print_mat(mat):
    for arr in mat:
        vet = list(map(lambda n: ("   " + str(n))[-3:], arr))
        print(*vet, sep=" ")
    print()


def loop_print(entrada):
    while entrada != 0:
        print_mat(matriz(entrada))
        entrada = int(input())


loop_print(int(input()))
