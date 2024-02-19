import re

str = 'номера машин A123BC78 и X666XX178'
print(re.findall(r'[A-Za-z]\d{3}[A-Za-z]+\d{2,3}', str))