import functools as fn


def soma_idade():
    array = []
    while True:
        entrada = int(input())
        if entrada < 0:
            break
        else:
            array.append(entrada)
        continue
    return f"{fn.reduce(lambda a, b: a + b, array)/len(array):.2f}"


print(soma_idade())
