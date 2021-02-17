def ent():
    inp = input().split()
    inp = [int(x) for x in inp]
    return inp

def volt():
    inp = ent()
    equip = {2: 1.25,
           3: 2.25,
           4: 3.25,
           5: 4.25,
           6: 5.25}
    total = 0
    for n in inp:
        total+= equip[n]
    return int(total)

print(volt())