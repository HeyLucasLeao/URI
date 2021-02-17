import datetime
while True:
    try:
        pe, dt = [int(x) for x in input().split()]
        inp = [[x for x in input().split()] for _ in range(dt)]
        datas = [x[0] for x in inp]
        disp = [x[1:] for x in inp]
        dicionario = dict([(x, y)
                           for x, y in zip(datas, disp) if not y.count('0') > 0])
        if len(dicionario) == 1:
            print(list(dicionario)[0])
        elif len(dicionario) >= 1:
            dicionario = list(dicionario)
            dicionario.sort(
                key=lambda date: datetime.datetime.strptime(date, "%d/%m/%Y"))
            print(dicionario[0])
        else:
            print('Pizza antes de FdI')
    except EOFError:
        break
