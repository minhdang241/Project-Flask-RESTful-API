import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

drop_table = "DROP TABLE users"

cursor.execute(drop_table)

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name VARCHAR(30), password VARCHAR(30))"
cursor.execute(create_table)


insert_query = "INSERT INTO users VALUES (?, ?, ?)"

users = [
    (1, 'jose', 'asdf'),
    (2, 'roft', 'asdf'),
    (3, 'anne', 'xyz')
]

cursor.executemany(insert_query, users)

# select_query = "SELECT * FROM users"
# for row in cursor.execute(select_query):
#     print(row)

connection.commit()
connection.close()