def factorial():
    N = int(input())
    if N > 13 or N < 0:
        raise Exception("erro")
    result = N
    i = N - 1
    while i > 0:
        result *= i
        i -= 1
    return result


print(factorial())
