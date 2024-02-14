c = [i for i in range(int(input()))]
def ch_plndrm(c):
    proverka = 0
    for i in c:
        ii = i
        while i > 0:
            ostatok = i % 10
            proverka = proverka*10 + ostatok
            i = i // 10
        if proverka == ii:
            proverka = 0
            yield ii
        else:
            proverka = 0

g = ch_plndrm(c)
for j in g:
    print(j, end=' ')