from math import comb


def chances():
    n, k, p = [int(x) for x in input().split()]
    p = p/100
    q = 1 - p
    res = round((comb(n, k) * (p ** k) * (q**(n - k)))*100, 2)
    return res


for i in range(int(input())):
    print(f"A chance de Basy acertar o numero no dia {i + 1} eh {chances()}%")
