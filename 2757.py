inp = [int(input()) for _ in range(3)]
a, b, c = [str(x) for x in inp]


def space(x):
    txt = " "*(10 - len(x))
    return txt + x


def zero(x):
    txt = "0"*(10 - len(x))
    arr = []
    arr.extend(txt)
    arr.extend(x)
    if '-' in arr:
        arr.remove('-')
        arr[0] = '-0'
    return "".join(x for x in arr)


def left(x):
    txt = " "*(10 - len(x))
    return x + txt


print(f"A = {a}, B = {b}, C = {c}")
print(f"A = {space(a)}, B = {space(b)}, C = {space(c)}")
print(f"A = {zero(a)}, B = {zero(b)}, C = {zero(c)}")
print(f"A = {left(a)}, B = {left(b)}, C = {left(c)}")
