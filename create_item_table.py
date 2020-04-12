import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

drop_table = "DROP TABLE IF EXISTS items"

cursor.execute(drop_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name VARCHAR(30), price REAL)"
cursor.execute(create_table)


insert_query = "INSERT INTO items VALUES (NULL, ?, ?)"

items = [
    ('chair', 9.99),
    ('table', 20),
    ('desk', 100)
]

cursor.executemany(insert_query, items)

# select_query = "SELECT * FROM users"
# for row in cursor.execute(select_query):
#     print(row)

connection.commit()
connection.close()