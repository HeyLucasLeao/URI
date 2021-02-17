def crow():
    caw = 3
    print_num = []
    num = 0
    while caw > 0:
        inp = input()
        if inp == "caw caw":
            print_num.append(num)
            caw -= 1
            num = 0
            continue
        else:
            inp = [x for x in inp] if len(inp) == 3 else False
            num += 4 if inp[0] == "*" else False
            num += 2 if inp[1] == "*" else False
            num += 1 if inp[2] == "*" else False
    return print_num


print(*crow(), sep="\n")
