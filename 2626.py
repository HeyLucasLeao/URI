def game():
    jogo = {'pedra': 0,
            'papel': 1,
            'tesoura': 2}
    vencedor = {0: 'Os atributos dos monstros vao ser inteligencia, sabedoria...',
                1: "Iron Maiden's gonna get you, no matter how far!",
                2: 'Urano perdeu algo muito precioso...',
                3: "Putz vei, o Leo ta demorando muito pra jogar..."}

    matriz = [[0, 0, 1, 1], [0, 2, 2, 0], [2, 1, 1, 2]]
    dodo, leo, pepper = input().split()
    resp = [jogo[dodo], jogo[leo], jogo[pepper]]

    for resultado in matriz:
        if not len(set(resp)) == 2:
            return vencedor[3]
        elif sorted(resp) == sorted(resultado[:3]):
            return vencedor[resp.index(resultado[3])]
    return vencedor[3]


while True:
    try:
        print(game())
    except EOFError:
        break
