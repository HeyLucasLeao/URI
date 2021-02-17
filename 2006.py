def conv_dados():
    cha = int(input())
    comp = input().split()
    comp = [int(x) for x in comp]
    return [cha, comp]


def ver(array=None):
    if not array:
        array = conv_dados()
    cha, comp = array
    if cha in comp:
        return comp.count(cha)
    else:
        return "0"


print(ver())
