import datetime as dt


def conv_d():
    inp = input().split()
    inp = [int(x) for x in inp]
    inp = [dt.timedelta(hours=x) for x in inp]
    a, b, c = inp
    res = dt.timedelta.total_seconds(a + b + c) / 3600
    return int(res)


def print_res(x=None):
    if not x:
        x = conv_d()
    if x >= 24:
        x -= 24
    elif x < 0:
        x += 24
    return x


print(print_res())
