def count():
    inp = int(input())
    return 0 if inp % 2 == 0 else 1


def loop(i=int(input())):
    print_result = []
    for x in range(i):
        print_result.append(count())
    return print_result


print(*loop(), sep="\n")
