def dados():
    inp, mult = input().split()
    mult = int(mult)
    inp = [x for x in inp]
    idx = 0
    ult = 0
    ignorar_idx = []
    ult_casa = 0
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
            inp[0] = '9'
        elif inp[i] == "?":
            inp[i] = '9'
    inp = [int(x) for x in inp]

    return inp, mult, idx, ult, ignorar_idx


def get_digit(number, n):
    return number // 10**n % 10


def verificar():
    inp, mult, idx, ult, ignorar_idx = dados()
    res = int("".join([str(x) for x in inp]))
    nres = res
    while not int("".join([str(x) for x in inp])) % mult == 0:
        print(inp)
        if inp[ult] == 0:
            for y in range(len(inp[:idx])):
                if inp[y] == 0 and not y in ignorar_idx:
                    inp[y] = 9
                    continue
                elif not y in ignorar_idx:
                    inp[y] -= 1
                    break
        else:
            inp[ult] -= 1
    return inp


print(verificar())
