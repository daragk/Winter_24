c = [i for i in range(1, int(input()))]

def s_minusom(l):
    for i in l:
        if i%2:
            yield i
        else:
            yield (-i)

g = s_minusom(c)
for j in g:
    print(j, end=' ')
