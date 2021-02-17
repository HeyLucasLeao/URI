# 2x3
# c1. cada duas interações, c1+=1
# c2. cada interação. c2 +=1, Cada duas, c2+= c1*2
# c3. cada interação. c3 +=1. Cada duas, c2*c1


def senq(entrada):
    i = 1
    countdown = 0
    array = [[1, 1, 1]]
    while countdown < entrada:
        array.append([array[-1][0], array[-1][1] + 1, array[-1][2] + 1])
        i += 1
        countdown += 1
        if countdown == entrada:
            break
        if i == 2:
            array.append([array[-1][0] + 1, array[-1][1] + array[-1]
                          [0]*2, (array[-1][1] + array[-1]
                                  [0]*2) * (array[-1][0] + 1)])
            i = 1
    return array


def print_array(array):
    for list in array:
        print(*list)


print_array(senq(int(input())))
