def temp():
    ano = int(input())
    conv = -2015
    conv += ano
    return f"{abs(conv)} D.C." if ano < 2015 else f"{abs(conv) + 1} A.C."


def loop_temp(inp = int(input())):
    result = []
    for i in range(inp):
        result.append(temp())
    return result

print(*loop_temp(), sep = "\n")
