def convert_input():
    a, b, c = input().split(" ")
    a, b, c = (int(x) for x in (a, b, c))
    return a, b, c


def inv():
    a, b, c = convert_input()
    dif_a = b - a
    dif_b = c - b
    smile = ":)"
    sad = ":("
    if a > b <= c or a < b < c and dif_b > dif_a or a == b < c \
            or a > b > c and dif_b > dif_a:
        return smile
    elif c <= b > a or c > b > a and dif_b < dif_a or \
            a > b > c and dif_a >= dif_b or a == b > c or a == b == c:
        return sad


print(inv())
