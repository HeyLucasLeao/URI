import re
while True:
    try:
        ent = (int(x) for x in input().split())
        _, y = ent
        tradu = input()
        cripto = input()
        tradu = tradu.lower()
        cripto = cripto.lower()
        txt = ""
        for _ in range(y): txt += input() + '\n'

        def to_unicode(inp: str) -> str: return ''.join(format(ord(x)) for x in inp)

        dicionario = dict(tuple((x, y) for x, y in zip(cripto, tradu)))
        dici_upper = dict(tuple((x, y) for x, y in zip(cripto.upper(), tradu.upper())))
        dici_inve = dict(tuple((x, y) for x, y in zip(tradu.upper(), cripto.upper())))
        
        def descripto(txt: str) -> str:
            res = txt
            for cripto,tradu in dicionario.items():
                res = re.sub(f"[{cripto}]+",f"_{to_unicode(tradu)}_",res)
                res = re.sub(f"[{tradu}]+", cripto,res)
                res = re.sub(f"_{to_unicode(tradu)}_", tradu,res)
            for i in range(len(res)):
                if res[i].isupper() and res[i] in dici_upper.keys():
                    res = res[:i] + dici_upper[res[i]] + res[i + 1:]
                elif res[i].isupper() and res[i] in dici_inve.keys():
                    res = res[:i] + dici_inve[res[i]] + res[i + 1:]
            return res

        print(descripto(txt))
    except:
        break
        
