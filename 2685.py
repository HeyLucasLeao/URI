def ver_hora():
    inp = int(input())
    if inp < 90:
        return 'Bom Dia!!'
    elif 180 > inp >= 90:
        return 'Boa Tarde!!'
    elif 270 > inp >= 180:
        return 'Boa Noite!!'
    elif 360 > inp >= 270:
        return 'De Madrugada!!'
    else:
        return 'Bom Dia!!'


while True:
    try:
        print(ver_hora())
    except EOFError:
        break
