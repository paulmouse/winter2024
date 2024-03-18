def sort(lst):
    n = len(lst)
    for i in range(n):
        #print(i)
        for j in range(0, n-i-1):
            # print(j)
            # print('----')
            # print(n-i-1)
            # print(lst[j])
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

        print(lst)

num = [3,42,64, 25, 12, 22, 11]
sort(num)
print(num)