def ppa():
    atk = {'ataque': 1, 'pedra': 2, 'papel': 3, 'tesoura': 4}
    p_um = input()
    p_dois = input()
    if atk[p_um] == 1 == atk[p_dois]:
        return f"Aniquilacao mutua"
    elif atk[p_um] == 3 == atk[p_dois]:
        return f"Ambos venceram"
    elif atk[p_dois] == 2 == atk[p_um]:
        return f"Sem ganhador"
    elif atk[p_dois] % atk[p_um] == 0:
        return f"Jogador 1 venceu"
    elif atk[p_um] % atk[p_dois] == 0:
        return f"Jogador 2 venceu"
    elif atk[p_dois] % atk[p_um] > atk[p_um] % atk[p_dois]:
        return f"Jogador 2 venceu"
    else:
        return f"Jogador 1 venceu"

def print_func(x = None):
    res = []
    if not x:
        x = int(input())
    for i in range(x):
        res.append(ppa())
    return res


print(*print_func(),sep = "\n")


