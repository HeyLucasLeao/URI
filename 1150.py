def ultra_z():
    x = int(input())
    z = int(input())
    while x >= z:
        z = int(input())
    x_i = x
    z_i = z
    result = 1
    while z_i >= x_i:
        x_i += x + result
        result += 1
    return result


print(ultra_z())
