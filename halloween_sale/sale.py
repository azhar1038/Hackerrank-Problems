def howManyGames(p, d, m, s):
    count=0
    while p >= m and s >= p:
        print('s', s, 'p', p)
        s -= p
        p -= d
        count += 1
    if s >= p+d:
        print('Still money left')
        count += s//m
    print('s', s)
    print(count)

print(howManyGames(20,3,6,50))