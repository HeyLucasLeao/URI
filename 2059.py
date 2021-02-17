def ques(inp=None):
    if not inp:
        inp = input().split()
        inp = [int(x) for x in inp]
    p, j1, j2, r, a = inp
    if r == 1 == a:
        return f"Jogador 2 ganha!"
    elif r != a:
        return f"Jogador 1 ganha!"
    elif (j1 + j2) % 2 == 0:
        return f"Jogador 1 ganha!" if 2 + p == 3 else \
            f"Jogador 2 ganha!"
    else:
        return f"Jogador 1 ganha!" if 2 + p != 3 else \
            f"Jogador 2 ganha!"


try:
    print(ques())
except:
    pass


