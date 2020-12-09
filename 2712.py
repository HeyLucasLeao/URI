def placa():
    matriz = [[1, 2, 'MONDAY'], [3, 4, 'TUESDAY'], [
        5, 6, 'WEDNESDAY'], [7, 8, 'THURSDAY'], [9, 0, 'FRIDAY']]
    inp = [x for x in input()]
    for i in range(4, len(inp)):
        try:
            inp[i] = int(inp[i])
        except ValueError:
            break
    if len(inp) == 8 and len([x for x in inp[:3] if x.isupper()]) == 3:
        for regra in matriz:
            if inp[-1] in regra[:2]:
                return regra[-1]
    return 'FAILURE'


[print(placa()) for _ in range(int(input()))]
