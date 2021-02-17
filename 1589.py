def somar_raio():
    a, b = input().split(" ")
    a, b = (int(x) for x in (a, b))
    return a + b


def loop(entrada):
    i = entrada
    while i > 0:
        print(somar_raio())
        i -= 1


loop(int(input()))
