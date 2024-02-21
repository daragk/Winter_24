import re

stroka = input().upper()

n_stroka = re.findall(r'\b\w{2,}', stroka)
for i in n_stroka:
    i = str(i)
    print(*re.findall(r'\b\w', i), end='')