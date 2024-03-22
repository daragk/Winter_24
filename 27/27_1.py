import numpy as np

n = int(input())
m = np.ones((n, n))
num = 2
start_col, start_row = 1, 1
end_col, end_row = n-2, n-2
k = (n // 2) + 1

for num in range(2, int(k) + 1):
# top
    for i in range(start_col, end_col+1):
        m[start_row][i] = num
# bottom
    for i in range(start_row, end_row+1):
        m[end_row][i] = num
# right
    for i in range(start_col, end_row+1):
        m[i][end_col] = num

# left
    for i in range(end_row, start_row-1, -1):
        m[i][start_col] = num

    start_col += 1
    start_row +=1
    end_col -= 1
    end_row -=1

print(m)

