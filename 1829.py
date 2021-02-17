def pref():
    a, b = input().split(" ")
    a, b = (int(x) for x in (a, b))
    q = a // b if b > 0 else (a // -b)*-1
    r = a % b if b > 0 else a % -b
    return q, r


print(*pref())
