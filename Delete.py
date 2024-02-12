import _sqlite3

conn = _sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("DELETE FROM EMPLOYEERS WHERE  ID =1")
conn.commit()

cursor = conn.execute("SELECT * FROM EMPLOYEERS")


for row in cursor:
    print(" ID :",row [0])
    print(" NAME :",row [1])
    print(" AGE:",row [2])
    print(" SALARY:",row [3])

print("Deleted successfully")
conn.close()