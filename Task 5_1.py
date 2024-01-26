n = int(input())

p = []
for i in range(n):
    rr = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            rr[j] = p[i-1][j-1] + p[i-1][j]
    p.append(rr)
    print(rr)
