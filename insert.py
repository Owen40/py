import sqlite3
conn=sqlite3.connect('listless.db')
print("Open database Successfull")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (1, 'Owen', 20,'Emobilis','Male')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (2, 'Solomon', 19,'Nyeri High','Male')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (3, 'Joanna', 18,'TUK','Female')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (4, 'Cynthia', 22,'UON','Female')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (5, 'Peter', 19,'MMU','Male')")
conn.execute("INSERT INTO wanafunzi(ID,NAME,AGE,SCHOOL,GENDER)VALUES (6, 'Karani', 20,'Emobilis','Male')")

conn.commit()
print("Records added successfully")
conn.close()