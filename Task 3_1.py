salaries = []
n = float(input())
while n != 0:
    salaries.append(n)
    n = float(input())
else:
    print(sum(salaries) / len(salaries))