def hamming(str1, str2):
    res = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            res += 1
    return res

s1 = 'abc'
# s2 = 'abx'
# s2 = 'axd'
# s2 = 'abc'
s2 = 'zxc'
res = hamming(s1, s2)
print(res)