import numpy as np
import pandas as pd

dct = {
    'Year': [2001, 2002, 2003, 2004, 2005],
    'Items': ['a', 'b', 'c', 'd', 'e'],
    'One': [10, 20, 30, 40, 50],
    'Price': [100, 200, 300, 400, 500]
}

df = pd.DataFrame(dct)
a = 0
for i in df.index:
    for j in df.columns:
        if type(df.loc[i, j]) == np.int64:
            a += df.loc[i, j]
print(f'Total sum is {a}')

for i in df.index:
    for j in df.columns:
        if type(df.loc[i, j]) == np.int64:
            a += df.loc[i, j]
    print(f'Сумма строки {i+1} = {a}')
    a = 0

for i in df.columns:
    a = df[i].sum()
    if type(a) == np.int64:
        print(f'Сумма столбца {i} = {a}')
