
def divisores():
    N = int(input())
    i = N
    array = []
    while i > 0:
        if (N % i == 0):
            array.append(i)
        i -= 1
    array.sort()
    for number in array:
        print(number)


divisores()
