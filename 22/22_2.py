bd = [(1,2), (1,3), (2,4), (2,5), (3,6), (3,7), (4,8), (4,9), (5,10)]

n_bd = sorted(bd, key=lambda x: x[1], reverse=True)
#print(n_bd)

counter = 0
tlx = n_bd[0][0]
for i in range(len(n_bd)):
    if n_bd[i][1] == tlx:
        counter += 1
        tlx = n_bd[i][0]

print(counter + 1)