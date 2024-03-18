import re
stroka = 'CAmEl caSe wOrD'

stroka = stroka.title()
print(re.sub(r' ', '', stroka))