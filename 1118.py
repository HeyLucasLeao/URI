# -*- coding: utf-8 -*-

import functools
array = []


def entradas(parameter: float):
    if parameter >= 0 and parameter <= 10:
        array.append(parameter)
        return array
    else:
        print(f"nota invalida")


def loop_entradas():
    while len(array) < 2:
        entradas(float(input()))


def print_result():
    loop_entradas()
    print(f"media = {functools.reduce(lambda a, b: (a+b)/2, array):.2f}")


while True:
    print_result()
    print("novo calculo (1-sim 2-nao)")
    res = int(input())
    while res != 1 and res != 2:
        print("novo calculo (1-sim 2-nao)")
        res = int(input())
    if res == 2:
        break
    array = []
