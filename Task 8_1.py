n = list(input().upper())

for i in range(len(n)-1):
    if n[i] == 'А' and n[i+1] == 'Г':
        n[i] = 'Г'
        n[i+1] = 'А'
    elif n[i] == 'Г' and n[i+1] == 'А':
        n[i] = 'А'
        n[i + 1] = 'Г'
    if n[i] == 'Ц' and n[i+1] == 'Т':
        inx = n.index('Ц')
        n.insert(inx+1, 'АГ')
    elif n[i] == 'Т' and n[i+1] == 'Ц':
        inx = n.index('Т')
        n.insert(inx+1, 'АГ')
print(''.join(n))
