import sqlite3

connection = sqlite3.connect('db.sqlite')


cursor = connection.cursor()

'''sql = "CREATE TABLE cliente (id integer, nome text, comentario text)"'''
id = 2
'''sql = f"SELECT * FROM cliente WHERE id={id}"'''

'''sql = "SELECT * FROM cliente"'''

sql = "INSERT INTO cliente (id, nome, comentario) VALUES (3, 'Jose', 'da peste!')"

cursor.execute(sql)

#rows = cursor.fetchall()

'''
for (id, nome, comentario) in rows:
    print("Valores: ", id, nome, comentario)
'''

connection.commit()
cursor.close()
connection.close()
