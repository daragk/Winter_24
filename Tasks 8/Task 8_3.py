n = input().split()

print(sorted(n, key=lambda j: len(list(set(j))), reverse=True))
