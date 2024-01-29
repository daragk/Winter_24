n = input()
tes1, tes2, tes3 = set(), set(), set()

for i in n:
    if i.isalpha():
        tes1.add(i)
    elif i.isdigit():
        tes2.add(i)
    elif not i.isalnum():
        tes3.add(i)

print(*tes1, '\n', *tes2, '\n', *tes3)
