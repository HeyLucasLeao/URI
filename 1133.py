# var
x = int(input())
y = int(input())

# functions


def senq():
    intervalo = [x, y]
    intervalo.sort()
    senq_resto = []
    i = intervalo[0]
    while i < intervalo[-1]:
        if i % 5 == 2 and i != intervalo[0] or i % 5 == 3 and i != intervalo[0]:
            senq_resto.append(i)
        i += 1
    return list(map(print, senq_resto))


# commands

senq()
