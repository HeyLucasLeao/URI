def primo(res):
    if res == 2:
        return "You’re a coastal aircraft, Robbie, a large silver aircraft."
    elif res < 2:
        return "Bad boy! I’ll hit you."
    else:
        test = list(range(2, res))
    if res % 2 == 0:  # par
        test = [x for x in test if x % 2 == 0]
        for n in test:
            if res % n == 0:
                return "Bad boy! I’ll hit you."
        return "You’re a coastal aircraft, Robbie, a large silver aircraft."
    elif res % 2 != 0:  # impar
        test = [x for x in test if x % 2 != 0]
        for n in test:
            if res % n == 0:
                return "Bad boy! I’ll hit you."
        return "You’re a coastal aircraft, Robbie, a large silver aircraft."


while True:
    try:
        x = int(input())
        inp = [int(input()) for _ in range(x)]
        pulos = int(input())
        inp.sort(reverse=True)
        lista = [inp[i] for i in range(0, len(inp), pulos)]
        res = sum(lista)
        print(primo(res))
    except EOFError:
        break
