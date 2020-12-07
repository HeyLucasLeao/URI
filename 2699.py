def dados():
    inp, mult = input().split()
    mult = int(mult)
    inp = [x for x in inp]
    idx = 0
    ult = 0
    ignorar_idx = []
    for x in range(len(inp)):  # última casa decimal
        if inp[x] == '?':
            ult = x
            break
    for x in range(len(inp)):  # índices a serem ignorados
        if not inp[x] == '?':
            ignorar_idx.append(x)
    for x in reversed(range(len(inp))):  # primeira casa decimal a mexer
        if not x in ignorar_idx:
            idx = x
            break
    for i in range(len(inp)):
        if inp[0] == "?":
            inp[0] = '1'
        elif inp[i] == "?":
            inp[i] = '0'
    inp = [int(x) for x in inp]
    return inp, mult, idx, ult, ignorar_idx


def get_digit(number, n):
    return number // 10**n % 10


def verificar():
    inp, mult, idx, ult, ignorar_idx = dados()
    res = int("".join([str(x) for x in inp]))
    while not res % mult == 0:
        if get_digit(res, len(inp) - ult - 1) == 9:
            return '*'
        elif get_digit(res, len(inp) - idx - 1) == 9:
            res -= 9*10**(len(inp) - idx - 1)
            for y in reversed(range(len(inp[:idx]))):
                if get_digit(res, len(inp) - y - 1) == 9 and not y in ignorar_idx:
                    res -= 9*10**(len(inp) - y - 1)
                    continue
                elif not y in ignorar_idx:
                    res += 10**(len(inp) - y - 1)
                    break
        else:
            res += 10**(len(inp) - idx - 1)
    return res


print(verificar())
