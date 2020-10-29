import re

ent = (int(x) for x in input().split())
_, y = ent
tradu = input()
cripto = input()
txt = ""

for _ in range(y):
    txt += input() + '\n'

iter_cripto = tuple((x, y) for x, y in zip(cripto,tradu))

def convert_to_binary_str(inp: str) -> str:
    return (''.join(format(ord(x), 'b') for x in inp))


def regex_to_lower(txt: str) -> str:
    res = txt
    for cripto,tradu in iter_cripto:
        res = re.sub(f"[{cripto.lower()}]+",f"_{convert_to_binary_str(tradu.lower())}_",res)

    for cripto,tradu in iter_cripto:
        res = re.sub(f"[{tradu.lower()}]+", cripto.lower(),res)

    for cripto,tradu in iter_cripto:
        res = re.sub(f"_{convert_to_binary_str(tradu.lower())}_", tradu.lower(),res)
    return res
    
def regex_to_upper(res: str) -> str:
    for cripto,tradu in iter_cripto:
        res = re.sub(f"[{cripto.upper()}]+",f"_{convert_to_binary_str(tradu.upper())}_",res)

    for cripto,tradu in iter_cripto:
        res = re.sub(f"[{tradu.upper()}]+", cripto.upper(),res)

    for cripto,tradu in iter_cripto:
        res = re.sub(f"_{convert_to_binary_str(tradu.upper())}_", tradu.upper(),res)
    return res

def descripto(inp: str) -> str:
    return regex_to_upper(regex_to_lower(inp))



print(descripto(txt))
