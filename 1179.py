def print_vet(vet, name="impar"):
    for i in range(len(vet)):
        print(f"{name}[{i}] = {vet[i]}")


try:
    par = []
    impar = []
    for n in range(0, 15):
        x = int(input())
        if x % 2 == 0:
            par.append(x)
        else:
            impar.append(x)

        if len(impar) > 4 or n == 14:
            print_vet(impar)
            impar = []
        if len(par) > 4 or n == 14:
            print_vet(par, "par")
            par = []
except ValueError:
    pass
