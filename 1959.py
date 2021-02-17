import functools as fn

inp = input().split()
inp = [int(x) for x in inp]
print(fn.reduce(lambda x, y: x * y, inp))
