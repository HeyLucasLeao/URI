def ver_hora():
    inp = float(input())
    hora = inp*24*10/3600 % 60
    minutos = inp*24*10/60 % 60
    segundos = inp*24*10 % 60
    resp = f"{int((hora + 6) % 24):02d}:{int(minutos):02d}:{int(segundos):02d}"
    if inp < 90:
        return f"Bom Dia!!\n{resp}"
    elif 180 > inp >= 90:
        return f"Boa Tarde!!\n{resp}"
    elif 270 > inp >= 180:
        return f"Boa Noite!!\n{resp}"
    elif 360 > inp >= 270:
        return f"De Madrugada!!\n{resp}"
    else:
        return f"Bom Dia!!\n{resp}"


while True:
    try:
        print(ver_hora())
    except EOFError:
        break
