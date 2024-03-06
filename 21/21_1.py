import pandas as pd
from random import random, randint, choice

total_tasks = 20 * 3 + 1

students = pd.DataFrame(columns=['Name', 'done_tasks', 'wrong_tasks', 'favourite_topic',
                                 'missing_lessons', 'payment'], index=range(10))
topics = ['ООП', 'Pandas', 'Numpy', 'SQL', 'Cycles', 'Functions']
x = 0
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'a', 'c']
for name in names:
    dt = randint(1, total_tasks)
    wt = total_tasks - dt
    f = choice(topics)
    m = randint(0, 10)
    op = randint(0, 1)
    students.iloc[x] = [name, dt, wt, f, m, op]
    x += 1
print(students)
