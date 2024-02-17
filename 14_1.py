nn = int(input("Enter your number: "))
def c_ch(n):
    if len(str(n)) == 1:
        return 1
    else:
        return 1 + c_ch(n // 10)

print(c_ch(nn))