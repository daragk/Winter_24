stroka = input()
stroka = list(stroka.split())
print(max(stroka, key=len))
