est = int(input())
ent = input().split()
ent = [int(x) for x in ent]
q_ent = ent.copy()
picked = 0
n = 0

while n <= len(q_ent):
    try:
        if n == -1:
            break
        elif q_ent[n] == 0:
            n += 1
            continue
        elif q_ent[n] % 2 != 0:
            picked += 1
            q_ent[n] -= 1
            n += 1
        else:
            for i in reversed(range(n + 1)):
                if q_ent[i] % 2 == 0 == i:
                    q_ent[i] -= 1 if q_ent[i] > 0 else False
                    n = i - 1
                    picked += 1 if q_ent[i] > 0 else False
                    break
                elif q_ent[i] == 0:
                    continue
                elif q_ent[i] % 2 == 0:
                    picked += 1
                    q_ent[i] -= 1
                    n = i - 1
    except IndexError:
        break

dif = [x for x, y in zip(ent, q_ent) if x == y]

print(len(q_ent) - len(dif), sum(q_ent))
