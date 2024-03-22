def countElements(lst):
    count = 0
    for i in lst:
        # print(i)
        if isinstance(i, list):
            # print(i)
            count += countElements(i)+1
        else:
            count += 1
    return count

# [1, 2, 3]
# ["x", "y", ["z"]]
# [1, 2, [3, 4, [5]]]

res = countElements(["x", "y", ["z"]])
print(res)