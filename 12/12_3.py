vvod = '1-2,4-4,3-6'

vvod = vvod.split(',')
print(vvod)
res = []

for i in vvod:
    rs = [j for j in range(int(i[0]), int(i[-1])+1)]
    res.extend(rs)

print(res)