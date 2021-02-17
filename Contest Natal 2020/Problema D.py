_ = input()
inp = [int(x) for x in input().split()]
inp.sort()
brinquedo = 1
n = 1
for i in range(1, len(inp)):
    if inp[i] > inp[i - 1]:
        n += 1
    brinquedo += 1*n
print(brinquedo)
