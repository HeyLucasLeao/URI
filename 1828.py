def tesoura_pedra():
    if sheldon == "pedra" and ray == "tesoura":
        return True
    if sheldon == "tesoura" and ray == "pedra":
        return False
    if sheldon == "tesoura" and ray == "papel":
        return True
    if sheldon == "papel" and ray == "tesoura":
        return False
    if sheldon == "papel" and ray == "pedra":
        return True
    if sheldon == "pedra" and ray == "papel":
        return False
    if sheldon == "pedra" and ray == "lagarto":
        return True
    if sheldon == "lagarto" and ray == "pedra":
        return False
    if sheldon == "lagarto" and ray == "Spock":
        return True
    if sheldon == "Spock" and ray == "lagarto":
        return False
    if sheldon == "Spock" and ray == "tesoura":
        return True
    if sheldon == "tesoura" and ray == "Spock":
        return False
    if sheldon == "tesoura" and ray == "lagarto":
        return True
    if sheldon == "lagarto" and ray == "tesoura":
        return False
    if sheldon == "lagarto" and ray == "papel":
        return True
    if sheldon == "papel" and ray == "lagarto":
        return False
    if sheldon == "papel" and ray == "Spock":
        return True
    if sheldon == "Spock" and ray == "papel":
        return False
    if sheldon == "Spock" and ray == "pedra":
        return True
    if sheldon == "pedra" and ray == "Spock":
        return False


def duelo(i):
    if tesoura_pedra() is True:
        return f"Caso #{i}: Bazinga!"
    elif tesoura_pedra() is False:
        return f"Caso #{i}: Raj Trapaceou!"
    else:
        return f"Caso #{i}: De novo!"


try:
    entrada = int(input())
    i = 1
    while entrada >= i:
        [sheldon, ray] = input().split(" ")
        print(duelo(i)
        i += 1
except:
    pass
