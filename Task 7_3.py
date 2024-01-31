mn = [[6, 2, 6], [4, 5, 3]]

def massiv7(n, m):
    res = []
    for i in range(n):
        for j in range(m):
            res.append(mn[i][j])
    res = list(set(res))

    print(res[-1:-4:-1])


massiv7(2, 3)
