album = {0: 'PROXYCITY',
         1: 'P.Y.N.G.',
         2: 'DNSUEY!',
         3: 'SERVERS',
         4: 'HOST!',
         5: 'CRIPTONIZE',
         6: 'OFFLINE DAY',
         7: 'SALT',
         8: 'ANSWER!',
         9: 'RAR?',
         10: 'WIFI ANTENNAS'}

res = [sum([int(x) for x in input().split()]) for _ in range(int(input()))]

[print(album[x]) for x in res]
