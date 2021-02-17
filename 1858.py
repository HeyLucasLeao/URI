def resp():
    entradas = input()
    inp = input().split(" ")
    inp = [int(x) for x in inp]
    min_inp = inp.index(min(inp)) + 1
    return min_inp

print(resp())