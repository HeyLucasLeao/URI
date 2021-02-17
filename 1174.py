try:
    for i in range(0, 100):
        x = float(input())
        if (x > 10):
            continue
        print(f"A{[i]} = {x:.1f}")
except:
    pass
