def mel_ar():
    pi = 3.14
    v = float(input())
    d = float(input())
    ar = pi * ((d / 2) ** 2)
    al = v / ar
    return f"ALTURA = {al:.2f}\nAREA = {ar:.2f}"

while True:
    try:
        print(mel_ar())
    except EOFError:
        break