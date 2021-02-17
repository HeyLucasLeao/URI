x = int(input())
y = [int(x) for x in input().split()]
if sum(y) > x:
    print("Deixa para amanha!")
else:
    print("Farei hoje!")
