
def convert_dados():
    inp = input().split(" ")
    PA = int(inp[0])
    PB = int(inp[1])
    G1 = float(inp[2])
    G2 = float(inp[3])
    return [PA, PB, G1/100, G2/100]


def comparativo(array):
    result_PA = array[0]
    result_PB = array[1]
    G1 = array[2]
    G2 = array[3]
    i = 0
    while result_PB >= result_PA:
        result_PA += int(G1*result_PA)
        result_PB += int(G2*result_PB)
        i += 1
        if i > 100:
            return "Mais de 1 seculo."
    return (f"{i} anos.")


def pergunta(entrada):
    i = 0
    while entrada > i:
        print(comparativo(convert_dados()))
        i += 1


pergunta(int(input()))
