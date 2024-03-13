import psycopg2
import openpyxl



# connect = psycopg2.connect(dbname="postgres", host="localhost", user="postgres", password="spiritof69", port="5432")
# cur = connect.cursor()
# cur.execute('''SELECT author, title FROM book''')
# rows = cur.fetchall()
# desc = cur.description # описаниия имена столбцов
#
# xlfile = '../files/sqltoXls.xlsx'
# wb = openpyxl.Workbook()
# ws = wb.active
# ws.append(['title'])
# for row in cur:
#      print(row)
#      ws.append(row)
#
# wb.save(xlfile)

# connect = psycopg2.connect(dbname="postgres", host="localhost", user="postgres", password="spiritof69", port="5432")
# cur = connect.cursor()
# cur.execute('''SELECT author, title, (100-amount) as supply
# 	           FROM book
#                WHERE amount < 100''')
# rows = cur.fetchall()
# # desc = cur.description # описаниия имена столбцов
# s = 0
# for row in rows:
#      print(f'{row[0]:15} {row[1]:30} {row[2]:5}')
#      s += int(row[2])
#      # cur.execute('''SELECT author, title, (100-amount) as supply
#      # 	           FROM book
#      #                WHERE amount < 100''')
# print(f'{s}')


import sqlite3

connection = sqlite3.connect('test.db')
cur = connection.cursor()
# cur.execute('''CREATE TABLE users
# (id INTEGER PRYMARY KEY,
# username TEXT,
# age INTEGER
# )''')
# cur.execute('''INSERT INTO users VALUES
# (1, 'username1', 15), (2, 'username2', 19)
# ''')
cur.execute('''SELECT * FROM users 
''')
users = cur.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()


