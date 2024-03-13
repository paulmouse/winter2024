import itertools

def combination(nums):
    max_num = 0
    for i in itertools.permutations(nums):
        num = int(''.join(map(str, i)))
        max_num = max(max_num, num)
    return max_num

# [9, 81, 25,92]
# [9, 81, 25,]
# [9, 81, 25,52,6,87]
# [1, 21, 3,]
lst = [9, 81, 25,52,6,87,99]

res = combination(lst)

print(res)