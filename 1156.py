s = 0
num = 1
dem = 1
while num <= 39:
    s += (num)/(dem)
    num += 2
    dem *= 2

print(f"{s:.2f}")
