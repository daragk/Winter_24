#Task 1_3
x = float(input())
y = float(input())

a = [x + y, x - y, x * y, x / y, x // y]

naibolshee = max(a)

if naibolshee == x + y:
    if x - y > x * y and x - y > x / y and x - y > x // y:
        print(x-y)
    if x * y > x - y and x * y > x / y and x * y > x // y:
        print(x * y)
    if x / y > x - y and x / y > x//y and x / y > x * y:
        print(x/y)
    if x // y > x - y and x // y > x * y and x // y > x / y:
        print(x//y)

elif naibolshee == x - y:
    if x + y > x * y and x + y > x / y and x + y > x // y:
        print(x + y)
    if x * y > x + y and x * y > x / y and x * y > x // y:
        print(x * y)
    if x / y > x + y and x / y > x // y and x / y > x * y:
        print(x / y)
    if x // y > x + y and x // y > x * y and x // y > x / y:
        print(x // y)

elif naibolshee == x * y:
    if x - y > x + y and x - y > x / y and x - y > x // y:
        print(x - y)
    if x + y > x - y and x + y > x / y and x + y > x // y:
        print(x + y)
    if x / y > x - y and x / y > x // y and x / y > x + y:
        print(x / y)
    if x // y > x - y and x // y > x + y and x // y > x / y:
        print(x // y)

elif naibolshee == x / y:
    if x - y > x * y and x - y > x + y and x - y > x // y:
        print(x - y)
    if x * y > x - y and x * y > x + y and x * y > x // y:
        print(x * y)
    if x + y > x - y and x + y > x // y and x + y > x * y:
        print(x + y)
    if x // y > x - y and x // y > x * y and x // y > x + y and x // y != naibolshee:
        print(x // y)

else:
    if x - y > x * y and x - y > x / y and x - y > x + y:
        print(x - y)
    if x * y > x - y and x * y > x / y and x * y > x + y:
        print(x * y)
    if x / y > x - y and x / y > x + y and x / y > x * y:
        print(x / y)
    if x + y > x - y and x + y > x * y and x + y > x / y:
        print(x + y)

print(max(a))