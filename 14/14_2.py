nn = int(input("Enter your number: "))

def sumnch(n):
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + sumnch(n // 10)

print('Сумма цифр числа: ', sumnch(nn))