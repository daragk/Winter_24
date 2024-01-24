s1 = input()
s2 = input()

dct1 = {}
dct2 = {}

for i in s1:
  if i not in dct1:
    dct1[i] = 0
  dct1[i] += 1

for j in s2:
  if j not in dct2:
    dct2[j] = 0
  dct2[j] += 1

print(dct1 == dct2)