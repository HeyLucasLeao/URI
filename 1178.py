try:
    inp = float(input())
    result = inp
    for n in range(0, 100):
        print(f"N[{n}] = {result:.4f}")
        result /= 2
except:
    pass
