vo = 'аусыиэяюёе'
lst = ['кино', 'питон', 'дорога', 'поросенок', 'итог', 'титан', 'погост', 'идея']
sample = 'питон'
def similar(st):
    res = []
    for i in range(len(st)):
        if st[i] in vo:
            res.append(i)
    return res
sample_sim = similar(sample)
for i in lst:
    if similar(i) == sample_sim:
        print(i)