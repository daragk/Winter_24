n = int(input())
f = []
for i in range(n+1):
    if i < 2:
        k = 1
        f.append(k)
    else:
        k = f[i-1] + f[i-2]
        f.append(k)
print(f)
