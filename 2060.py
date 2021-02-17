t = input()
inp = input().split()
inp = [int(x) for x in inp]
for i in range(2,6):
    nums = [x for x in inp if x % i == 0]
    print(f"{len(nums)} Multiplo(s) de {i}")
