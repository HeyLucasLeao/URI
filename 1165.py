
def num_primo(x):
    num = []
    for n in range(1, x + 1):
        if (x % n == 0):
            num.append(n)
    if len(num) == 2:
        return f"{x} eh primo"
    else:
        return f"{x} nao eh primo"


def perguntar(entrada):
    i = 0
    while entrada > i:
        print(num_primo(int(input())))
        i += 1


perguntar(int(input()))
