lst = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4]

cur_max = max(lst)
cur_min = min(lst)

res = [i for i in range(len(lst)) if lst[i] == cur_max]
res2 = [i for i in range(len(lst)) if lst[i] == cur_min]
print(res2, res, sep=', ')
