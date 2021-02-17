inp = input().split(" ")
inp_int = list(map(int, inp))


def print_tabela():
    for i in range(1, inp_int[1] + 1):
        print(i, end=" ")
        if i % inp_int[0] == 0:
            print()


print_tabela()
