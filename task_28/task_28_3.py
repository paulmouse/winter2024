def hanoi(n, s1, s3, s2):
    if n == 1:
        print('1 :', s1, '->', s3)
        return 1
    count = 0
    count += hanoi(n-1, s1, s2, s3)
    print(n,':', s1, '->', s3)
    count += 1
    #count += hanoi(n - 1, s3, s2, s1)
    count += hanoi(n-1, s2, s3, s1)
    return count

n = 2
s1 = 's1'  # 1
s2 = 's2'  # 2
s3 = 's3'  # 3

res = hanoi(n, s1, s3, s2)
print(res)