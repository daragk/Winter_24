with open('test1.txt', 'r', encoding="utf-8") as f1:
    f1 = f1.readlines()
    for i in f1:
        print(i)

with open('test2.txt', 'w', encoding="utf-8") as f2:
    f2.writelines(f1)

with open('test2.txt', 'r', encoding="utf-8") as f2:
    f2 = f2.readlines()
    for i in f2[::-1]:
        i_s = i.split()
        print(*i_s[::-1])