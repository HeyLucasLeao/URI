try:
    inp = int(input())
    i = 0
    for n in range(0, 1000):
        if i > inp - 1:
            i = 0
        print(f"N[{n}] = {i}")
        i += 1
except:
    pass
