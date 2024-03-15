pr = 0
lv = 0
stroka = '())(()'

if stroka[0] == ")":
    print('incorrect')
else:
    for i in stroka:
        if i == '(':
            pr += 1
        else:
            lv += 1
        if lv > pr:
            break
    if lv != pr:
        print('incorrect')
    else:
        print('correct')


