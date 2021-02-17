def function(entrada):
    n = 1
    i = 0
    array = []
    while i < entrada:
        array.append([n, n**2, n**3])
        i += 1
        n += 1
    for list in array:
        print(*list)


function(int(input()))
