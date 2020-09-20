s1 = input()
s2 = input()

n = len(s1)
c = []
for _ in range(n+1):
    c.append([0]*(n+1))
for i in range(1, n+1):
    for j in range(1, n+1):
        if s1[i-1] == s2[j-1]:
            c[i][j] = c[i-1][j-1]+1
        else:
            c[i][j] = max(c[i-1][j], c[i][j-1])
print(c[-1][-1])