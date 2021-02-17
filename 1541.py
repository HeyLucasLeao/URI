def bob_construtor():
    area = a*b
    terreno = area*100/c
    terreno = int(terreno**.5)
    return terreno


while True:
    try:
        a, b, c = input().split(" ")
        a, b, c = (int(x) for x in (a, b, c))
        print(bob_construtor())
    except ValueError:
        break
    else:
        pass
