from math import floor
bolinhas = int(input())
galhos = int(input())
if galhos % 2 != 0:
    galhos = floor(galhos/2)
else:
    galhos = galhos/2
res = galhos - bolinhas
if res > 0:
    print(f"Faltam {int(res)} bolinha(s)")
else:
    print(f"Amelia tem todas bolinhas!")
