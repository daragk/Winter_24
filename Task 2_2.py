lst = [77,-2,108,1,2,3,4,5,6,7,8,9,109,-3,0.000007]
curr_min = lst[0]
for i in range(len(lst)):
    if curr_min > lst[i]:
        curr_min = lst[i]

print(curr_min)