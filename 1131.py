while True:
    try:
        qtd = int(input())
        inp = [[int(x) for x in input().split()] for _ in range(qtd)]
        value = 0
        for i in range(len(inp)):
            if inp[i][1]/inp[i][0] > value:
                value = inp[i][1]/inp[i][0]
                res = i + 1
                print(res)
    except EOFError:
        break
