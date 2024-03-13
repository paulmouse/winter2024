import psycopg2
connect = psycopg2.connect(dbname="postgres", host="localhost", user="postgres", password="***", port="5432")
cur = connect.cursor()
# cur.execute('''SELECT book_id, title, author, price FROM book''')
cur.execute('''SELECT * FROM book''')
rows = cur.fetchall()
title = [desc[0] for desc in cur.description]
# print(rows)
print(*title)
for row in rows:
    # print(*headers)
    print(*row)
    print('----')
