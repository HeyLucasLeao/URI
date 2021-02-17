try:
    vetor = []
    for i in range(0, 20):
        n = int(input())
        vetor.append(n)
    i = 0
    vetor.reverse()
    for n in vetor:
        print(f"N[{i}] = {n}")
        i += 1
except:
    pass
