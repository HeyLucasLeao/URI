def escala():
    inp = input()
    r, g, b = [int(x) for x in input().split()]
    if inp == 'min':
        return int(min(r, g, b))
    elif inp == 'mean':
        return int((r + g + b)/3)
    elif inp == 'max':
        return max(r, g, b)
    elif inp == 'eye':
        return int(.3*r + .59*g + .11*b)


def res():
    x = int(input())
    for i in range(x):
        res = escala()
        print(f"Caso #{i + 1}: {res}")


res()
