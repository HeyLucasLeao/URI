import sys
sys.stdout = open(sys.stdout.buffer.fileno(), 'w', encoding='utf8')


def checar_primo(n):
    if n <= 1:
        return "Bad boy! I’ll hit you."
    for x in range(2, n):
        if n % x == 0:
            return "Bad boy! I’ll hit you."
    return "You’re a coastal aircraft, Robbie, a large silver aircraft."


while True:
    try:
        x = int(input())
        inp = [int(input()) for _ in range(x)]
        pulos = int(input())
        lista = [inp[i] for i in range(0, len(inp), pulos)]
        res = sum(lista)
        print(checar_primo(res))
    except EOFError:
        break
