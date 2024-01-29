n = input().upper()

dct = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
       'C': 100, 'D': 500, 'M': 1000}
res = []
for i in n:
    res.append(dct[i])
res.append(0)
chs = 0
for j in range(len(res)-1):
    if res[j] >= res[j+1] or res[j+1] is None:
        chs += res[j]
    elif res[j] < res[j+1]:
        chs -= res[j]
print(chs)
