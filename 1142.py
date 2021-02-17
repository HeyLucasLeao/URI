def pums(entrada):
    pum_senq = []
    i = 1
    n = 1
    while i <= entrada:
        pum_senq.append([n, n + 1, n + 2, 'PUM'])
        i += 1
        n += 4
    for list in pum_senq:
        print(*list)


pums(int(input()))
