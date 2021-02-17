ent = input().split()
ent = [float(x) for x in ent]
ant,nov = ent
print(f"{(nov/ant - 1)*100:.2f}%")