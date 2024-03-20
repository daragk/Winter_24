def ravn(str1, str2):
    n = 0
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if n < 1:
                    n += 1
                else:
                    return False
        return True
    elif abs(len(str1) - len(str2)) == 1:
        if min(str1, str2, key= len) in max(str1, str2, key= len):
            return True
    else: return False

print(ravn('axc', 'abc'))
print(ravn('abc', 'acb'))
print(ravn('', '  '))
