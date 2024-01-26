n = int(input())
prst = []
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')
        prst.append(i)


