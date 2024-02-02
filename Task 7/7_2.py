def code(n, c):
    shifr = ''
    for i in range(len(n)):
        if n[i].islower() and (ord(n[i]) + c > ord('z')):
            nw = (ord('a') - 1) + (c - (ord(n[i]) - ord('z')))
            shifr += chr(nw)
        elif n[i].isupper() and ord(n[i]) + c > ord('Z'):
            nw = (ord('A') - 1) + (c - (ord(n[i]) - ord('Z')))
            shifr += chr(nw)
        else:
            nw = chr(ord(n[i])+c)
            shifr += nw
    print(shifr)
    return shifr

code('IlOvePythonZzZ', 3)
