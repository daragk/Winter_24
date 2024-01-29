s1, s2 = input().split(', '), input().split(', ')
res = []
for i in range(len(s1)):
    if s1[i] not in res and s1[i] in s2:
        res.append(s1[i])

print(f'Общих книг: {len(res)}')
