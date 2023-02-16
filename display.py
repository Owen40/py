import sqlite3
conn=sqlite3.connect('listless.db')
data=conn.execute("SELECT * FROM wanafunzi")
for row in data:
    print("Id=",row[0])
    print("Name=",row[1])
    print("Age=",row[2])
    print("School=",row[3])
    print("Gender=",row[4],"\n")
conn.close()