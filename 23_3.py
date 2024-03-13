import itertools

#n = [9, 81, 25]
n = [1,21,3]
ch = ''
s = []
for variant in itertools.permutations(n, len(n)):
    for element in range(len(n)):
        ch += str(variant[element])
    s.append(int(ch))
    ch = ''
print(max(s))