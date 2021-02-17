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
    if len(array) > 2:
        y = x
        k = 1
        while y > 1:
            for i in range(k, y - 1):
                for j in range(k, y - 1):
                    array[i][j] += 1
            y -= 1
            k += 1
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
