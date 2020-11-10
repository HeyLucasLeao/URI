import re
import operator as op
from typing import TypeVar, Dict

while True:
    try:
        qtd = int(input())
        arr = []
        resp = []
        arr = [re.split("[= ]+",input()) for _ in range(qtd)]
        arr = [[int(x) for x in y] for y in arr]
        resp = [input().split() for _ in range(qtd)]
        desclass = []

        ops: Dict[str,TypeVar('function')] = {'+': op.add, '-': op.sub,'*': op.mul}

        for x in range(len(arr)):
            for y in range(len(resp)):
                if int(resp[y][1]) - 1 == x:
                    if resp[y][2] == 'I' and ops['+'](arr[x][0],arr[x][1]) != arr[x][2] and ops['-'](arr[x][0],arr[x][1]) != arr[x][2] and ops['*'](arr[x][0],arr[x][1]) != arr[x][2]:
                        continue
                    elif resp[y][2] in ops and ops[resp[y][2]](arr[x][0],arr[x][1]) == arr[x][2]:
                        continue
                    else:
                        desclass.append(resp[y][0])
        desclass.sort()
        if len(desclass) == len(resp):
            print(f"None Shall Pass!")
        elif len(desclass) == 0:
            print(f"You Shall All Pass!")
        else:
            print(*desclass)
    except EOFError:
        break