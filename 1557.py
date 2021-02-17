def mat(x):
    array = []
    nested_list = []
    for i in range(x):
        nested_list.append([])
        for j in range(x):
            nested_list[i].append(1)
    array.extend(nested_list)
    return sum_interior(x, array)


def sum_interior(x, array):
    if len(array) > 1:
        k = 2
        for i in range(1, x):
            array[i][0] *= k
            array[0][i] *= k
            k *= 2
        for i in range(1, x):
            array[-1][i] *= array[-1][i - 1] * 2
        for i in range(1, x - 1):
            for j in range(1, x):
                array[i][j] *= array[i][j - 1] * 2
    return array


def print_mat(array):
    max_num = max(max(array))
    pat_str = " " * len(str(max_num))
    for arr in array:
        vet = list(map(lambda n: (pat_str + str(n))
        [-len(str(max_num)):], arr))
        print(*vet, sep=" ")
    print()


def loop_print(inp):
    while inp != 0:
        print_mat(mat(inp))
        inp = int(input())


loop_print(int(input()))
