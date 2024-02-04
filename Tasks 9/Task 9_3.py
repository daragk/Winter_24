n = input().lower()
dct = {}

for i in n:
    if not i.isalnum():
        continue
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] += 1

n_dct = sorted(dct.items(), key=lambda x: x[1], reverse=True)

for j in range(len(n_dct)):
    if j < 10:
        print(f'{n_dct[j][0]} - {n_dct[j][1]}')
