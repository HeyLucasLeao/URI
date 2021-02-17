def convert_input():
    try:
        n = int(input())
        x = list(map(int, input().split()))
        if n < 1 or len(x) < 1:
            raise ValueError
    except ValueError:
        print(f"Dados invalidos.")
    else:
        return x


def menor_pos(inp):
    x_desc = sorted(inp)
    menor_num = x_desc[0]
    pos_num = inp.index(menor_num)
    print(f"Menor valor: {menor_num}\nPosicao: {pos_num}")


try:
    menor_pos(convert_input())
except:
    pass
