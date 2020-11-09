from typing import List

while True:
    def to_unicode(inp: str) -> str: return ''.join(format(ord(x)) for x in inp)
    def descripto(txt: List[str]) -> List[str]:
            res = txt
            for i in range(len(res)):
                if res[i] in dicionario.keys():
                    res[i] = to_unicode(dicionario[res[i]])
            for i in range(len(res)):
                if res[i] in dicionario_invertido.keys():
                    res[i] = dicionario_invertido[res[i]]
            for i in range(len(res)):
                if res[i] in dicionario_unicode.keys():
                    res[i] = dicionario_unicode[res[i]]
            for i in range(len(res)):
                if res[i].isupper() and res[i] in dici_upper.keys():
                    res[i] = dici_upper[res[i]]
                elif res[i].isupper() and res[i] in dici_inve.keys():
                    res[i] = dici_inve[res[i]]
            return res
    try:
        ent = (int(x) for x in input().split())
        _, y = ent
        tradu = input()
        cripto = input()
        tradu = tradu.lower()
        cripto = cripto.lower()
        txt = ""
        for _ in range(y): txt += input() + '\n'
        txt = list(txt)


        arr_uni = [to_unicode(l) for l in tradu]

        dicionario = dict(tuple((x, y) for x, y in zip(cripto, tradu)))
        dicionario_unicode = dict(tuple((x, y) for x, y in zip(arr_uni, tradu)))
        dicionario_invertido = dict(tuple((x, y) for x, y in zip(tradu, cripto)))
        dici_upper = dict(tuple((x, y) for x, y in zip(cripto.upper(), tradu.upper())))
        dici_inve = dict(tuple((x, y) for x, y in zip(tradu.upper(), cripto.upper())))

        print(*descripto(txt), sep = "")
    except:
        break
