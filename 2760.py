from re import findall
a = input()
b = input()
c = input()
arr = [a, b, c]
final = ""

for word in arr:
    if findall(f"{word}", final):
        continue
    final += word[:10]

print(f"{a + b + c}")
print(f"{b + c + a}")
print(f"{c + a + b}")
print(f"{final}")
