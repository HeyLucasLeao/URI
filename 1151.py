def fibonacci():
    array = []
    entrada = int(input())
    i = 0
    if entrada > 46:
        raise Exception("valor acima de 46")
    while entrada > i:
        if len(array) > 1:
            array.append(array[-1] + array[-2])
        else:
            array.append(i)
        i += 1
    return array


print(*fibonacci())
