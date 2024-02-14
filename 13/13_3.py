lst = [i for i in range(int(input()))]

def nech(l):
     for i in l:
         if i%2:
             yield i

g = nech(lst)
for j in g:
    print(j)