def palindrome(st):
    st = st.replace(' ', '')
    if len(st) <= 1:
        return True
    else:
        if st[0] == st[-1]:
            return palindrome(st[1:-1])
        else:
            return False

print(palindrome('а роза упала на лапу азора'))
