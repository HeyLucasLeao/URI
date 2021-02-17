ent = int(input())
vagas = int(input())
inp = [int(input()) for _ in range(ent)]
ele = set(inp)
resp = inp.count(max(ele))
while vagas > resp:
    ele.remove(max(ele))
    resp += inp.count(max(ele))

print(resp)
