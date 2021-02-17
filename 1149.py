# 0 <= i <= N -1

def soma_a():
    input_prompt = input().split(" ")
    input_int = list(map(int, input_prompt))
    input_filter = list(filter(lambda x: x > 0, input_int))
    A = input_filter[0]
    N = input_filter[1]
    while N <= 0:
        N = int(input())
    i = 0
    result = 0
    while i <= N - 1:
        result += A + i
        i += 1
    return result
((()))
print(soma_a())

