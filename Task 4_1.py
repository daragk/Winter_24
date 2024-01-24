a = input().split()
if '+' in a:
    print(float(a[0]) + float(a[2]))
elif '-' in a:
    print(float(a[0]) - float(a[2]))
elif '/' in a:
    print(float(a[0]) / float(a[2]))
