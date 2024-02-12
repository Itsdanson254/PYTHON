import _sqlite3

conn = _sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("update EMPLOYEERS SET AGE = 40 where ID = 5")
conn.commit()

cursor = conn.execute("SELECT * FROM EMPLOYEERS")

for row in cursor:
    print(" ID :",row [0])
    print(" NAME :",row [1])
    print(" AGE:",row [2])
    print(" SALARY:",row [3])

print("Update done successfully")
conn.close()