# -*- coding: utf-8 -*-

import re

x = int(input())
for y in range(x):
    perigosos = [input() for _ in range(int(input()))]
    txt_perigosos = "\n".join(perigosos)
    experiencias = [input() for _ in range(int(input()))]
    output = []
    for compostos in experiencias:
        if re.findall(r"(?=("+'|'.join(perigosos)+r")(?![a-z0-9]))", compostos):
            output.append('Abortar')
        else:
            output.append('Prossiga')
    print(*output, sep="\n")
    if not y == x - 1:
        print()
