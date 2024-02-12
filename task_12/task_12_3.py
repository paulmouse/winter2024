s = input().split(',')
print(s)
# 1-2,3-4,3-16
res = []
for z in s:
    x,y = map(int,z.split('-'))
    print(x, y)
    for u in range(x,y+1):
        res.append(u)
print(res)