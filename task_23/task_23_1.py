def max_pal(s):
    len_s = len(s)
    for i in range(len_s, -1, -1):
        for j in range(len_s-i):
            ss = s[j:i+j+1]
            print(ss)
            if ss==ss[::-1]:
                return ss
s = input()
print(max_pal(s))