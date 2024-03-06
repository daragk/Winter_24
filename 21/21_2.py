import random
n = 4
m = [[random.randint(1, 100) for i in range(n)] for j in range(n)]
print(m)

way = 0
i = 0
j = 0

try:
    while i <= len(m) and j <= len(m):
        nachalo = m[i][j]
        if (m[i+1][j] + nachalo) < (m[i][j+1] + nachalo):
            way += nachalo
            i += 1
        elif (m[i+1][j] + nachalo) > (m[i][j+1] + nachalo):
            way += nachalo
            j += 1

except IndexError:
    while (i != len(m)) and (j != len(m)):
        nachalo = m[i][j]
        if (i == (len(m) - 1)) and (j != len(m)):
            way += nachalo
            j += 1
        else:
            way += nachalo
            i += 1
print(way)