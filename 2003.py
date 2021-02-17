import datetime as dt

def conv_inp():
    inp = input().split(':')
    inp = [int(x) for x in inp]
    inp = dt.timedelta(hours=inp[0], minutes=inp[1])
    return inp

def bino():
    dif = dt.timedelta(hours=8) - dt.timedelta(minutes = 60)
    res = int(dt.timedelta.total_seconds(conv_inp() - dif)/60)
    return f"Atraso maximo: {res}" if res >= 0 else "Atraso maximo: 0"

while True:
    try:
        print(bino())
    except EOFError:
        break