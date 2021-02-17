import functools as fn

def ent():
    inp = input().split()
    inp = [int(x) for x in inp]
    return inp


def tri():
    array = sorted(ent())
    print_tri = []
    for n in array:
        dif = [array[array.index(n) - 2], array[array.index(n) - 3]]
        dif.sort()
        if fn.reduce(lambda x,y: y + x,dif) > n > fn.reduce(lambda x,y: y - x,dif):
            print_tri.append([n, dif[0], dif[1]])
    return "S" if len(print_tri) > 0 else "N"


print(tri())

