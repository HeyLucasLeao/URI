inp = input().split()
inp = [int(x) for x in inp]

inp.append(inp[0]) if inp[0] > inp[1] else inp.append(inp[1])

print(inp[2])