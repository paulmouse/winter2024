# dict1 = {'яблоки': 100, 'бананы': 333, 'груши': 300,'апельсины': 300}
# dict2 = {'яблоки': 300, 'груши': 200, 'малина': 777, 'ананасы': 12}
# res = {}
# for key in dict1 | dict2:
#     res[key] = dict1.get(key, 0) + dict2.get(key, 0)
# print(res)

import psycopg2

# task_22_2

# tree = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7),(4, 8),(8, 9)]
# max_path , max_v =0,0
# for i, j in tree:
#     cur_path = 0
#     tf = True
#     while tf:
#         cur_path +=1
#         for x, y in tree:
#             if y == i:
#                 i == x
#                 break
#         else:
#             tf = False
#     print(j, cur_path)
#     input()
#     if cur_path > max_path:
#         max_path = cur_path
#         max_v = j
# print(max_path, max_v)


# tree = [(11,2), (11,3), (2,4), (2,5), (3,6), (6,7), (7,8), (8,9), (5,10)]
# tes = set([j for i,j in tree])
# for i, j in tree:
#     if i not in tes:
#         v = i
#         break
# p = {v:0}
# tf = True
# while tf:
#     tf = False
#     for i, j in tree:
#         if j not in p and i in p:
#             p[j] = p[i] + 1
#             tf = True
#             break
#     print(p)
#     input()
# print(max(p.values()))

# import psycopg2
# connect = psycopg2.connect(dbname="postgres", host="localhost", user="postgres", password="spiritof69", port="5432")
# cur = connect.cursor()
# cur.execute('''SELECT * FROM book
# WHERE author_id = 1''')
# rows = cur.fetchall()
# # print(rows)
# for row in rows:
#     print(f'{row[0]}', end=' ')
#     print(f'{row[1]}', end=' ')
#     print(f'{row[2]}', end=' ')
# table = 'book'
# cur.execute(f'''INSERT INTO {table} VALUES
# (12, 'На дне', 'Достоевский', 334, 34,0,0)''')


# connect.commit()
# connect.close()

import collections
a = collections.Counter('aabbccddcc')
print(f'{a=}')
b = dict(a)
print(b)