def seq(x=None):
    if not x:
        x = int(input())
    fac = [0]
    for i in range(x + 1):
        for n in range(i):
            fac.append(i)
    return fac


def print_result():
    i = 0
    bs = " "
    while True:
        try:
            res = seq()
            res = [str(x) for x in res]
            i += 1
            if len(res) == 1:
                print(f"Caso {i}: {len(res)} numero\n{bs.join(res)}\n")
            else:
                print(f"Caso {i}: {len(res)} numeros\n{bs.join(res)}\n")
        except EOFError:
            break


print_result()
