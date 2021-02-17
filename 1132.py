# var
x = int(input())
y = int(input())

# functions


def senq():
    intervalo = [x, y]
    intervalo.sort()
    senq_soma = []
    i = intervalo[0]
    while i <= intervalo[-1]:
        if i % 13 != 0:
            senq_soma.append(i)
        i += 1
    return sum(senq_soma)


# commands

print(senq())
