import _sqlite3

conn = _sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEERS  VALUES (1, 'Faith Karimi' ,23 ,345000.00)")
conn.execute("INSERT INTO EMPLOYEERS  VALUES (2, 'Bob Shimiruy' ,21 ,340000.00)")
conn.execute("INSERT INTO EMPLOYEERS  VALUES (3, 'John Kimasul' ,22 ,340000.00)")
conn.execute("INSERT INTO EMPLOYEERS VALUES (4, 'Faith Natumoi' ,26 ,300000.00)")
conn.execute("INSERT INTO EMPLOYEERS VALUES (5, 'Mark Njiroine' ,24 ,300000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()
