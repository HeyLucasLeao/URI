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


def verificar():
    inp, mult, idx, ult, ignorar_idx = dados()
    while not int("".join([str(x) for x in inp])) % mult == 0:
        print(*inp, sep="")
        if inp[ult] == 9:
            return '*'
        elif inp[idx] == 9:
            inp[idx] = 0
            for y in reversed(range(len(inp[:idx]))):
                if inp[y] == 9 and not y in ignorar_idx:
                    inp[y] = 0
                    continue
                elif not y in ignorar_idx:
                    inp[y] += 1
                    break
        else:
            inp[idx] += 1
    return inp


print(*verificar(), sep="")
