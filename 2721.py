renas = ['Dasher', 'Dancer', 'Prancer', 'Vixen',
         'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']
inp = [int(x) for x in input().split()]
inp = sum(inp)
i = 0
res = ''
for _ in range(inp):
    if i >= len(renas):
        i = 0
    res = renas[i]
    i += 1

print(res)
