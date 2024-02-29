import itertools

dengi = [10, 50, 100, 200, 500, 1000, 2000, 5000]
for j in range(len(dengi)):
    for i in itertools.combinations(dengi, j+1):
        print(i)