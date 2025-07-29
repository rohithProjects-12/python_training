import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="rohith_ece"  # the same DB name you're exploring in Workbench
)
cur = conn.cursor()
cur.execute("SHOW TABLES;")
tables = cur.fetchall()
for table in tables:
    print(table[0])
cur.close()
conn.close()
