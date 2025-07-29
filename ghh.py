import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="rohith_ece"
)
cursor = conn.cursor()
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()
print("Tables:", [t[0] for t in tables])

for table in tables:
    print(f"\nData from {table[0]}:")
    cursor.execute(f"SELECT * FROM {table[0]} LIMIT 10;")
    for row in cursor.fetchall():
        print(row)

cursor.close()
conn.close()
