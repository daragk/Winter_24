dct = {1:1, 2:2, 3:{2:22, 3:{1:111, 2: 222, 3:{1:1111, 2:2222, 3:3333}}}}
res = []
def znach(dct):
    x = 1 #int(input())
    for i in dct:
        if type(dct.get(i)) == int or type(dct.get(i)) == float():
            if i == x:
                res.append(dct.get(i))
        elif type(dct.get(i)) == dict:
            znach(dct.get(i))

znach(dct)
print(res)