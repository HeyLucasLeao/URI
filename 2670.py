a, b, c = [int(input()) for _ in range(3)]
print(min((b*2 + c*4), (a*2 + c*2), (a*4 + b*2)))
