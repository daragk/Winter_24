dct = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'T'
}
s = input().upper()
for i in s:
    print(dct[i], end='')