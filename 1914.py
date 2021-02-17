def jog():
    inp = input().split()
    num = input().split()
    num = [int(x) for x in num]
    return inp[inp.index("PAR") - 1] if sum(num) % 2 == 0 else inp[inp.index("IMPAR") - 1]


def loop(i=int(input())):
    print_result = []
    for x in range(i):
        print_result.append(jog())
    return print_result


print(*loop(), sep="\n")
