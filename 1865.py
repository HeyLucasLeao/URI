def ham():
    inp = input().split(" ")
    return "Y" if inp[0] == "Thor" else "N"


def loop(i):
    print_result = []
    for x in range(i):
        print_result.append(ham())
    return print_result


print(*loop(int(input())), sep="\n")