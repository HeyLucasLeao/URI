from math import sqrt
from dataclasses import dataclass
from typing import Dict


@dataclass
class Magia:
    dano: int
    level: Dict[int, int]


fire = Magia(200, {1: 20, 2: 30, 3: 50})
water = Magia(300, {1: 10, 2: 25, 3: 40})
earth = Magia(400, {1: 25, 2: 55, 3: 70})
air = Magia(100, {1: 18, 2: 38, 3: 60})


def menor_distancia(x1, x0, y1, y0) -> float:
    form = (x0 - x1)**2 + (y0 - y1)**2
    return round(sqrt(form), 2)


def golpe():
    dici = {'fire': fire, 'water': water, 'earth': earth, 'air': air}
    w, h, x0, y0 = [int(x) for x in input().split()]
    inp = input().split()
    var = inp[0]
    nivel, x1, y1 = [int(x) for x in inp[1:]]

    if dici[var].level[nivel] >= menor_distancia(x1, x0, y0, y1):
        return dici[var].dano
    else:
        return 0


output = []
for _ in range(int(input())):
    output.append(golpe())

print(*output, sep="\n")
