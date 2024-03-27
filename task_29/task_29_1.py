from collections import Counter
# lst = [2, 2, 2, 2, 7, 2, 2]
lst = [7, 2, 7, 7]

res =Counter(lst)

def get_key(res, value):
    for k, v in res.items():
        if v == value:
            return k


print(get_key(res, 1))
