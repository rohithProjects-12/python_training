import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="roottoor",
    database="rohith_ece"

mycursor = mydb.cursor(),
sql = "INSERT INTO user1 (id,name,email) "
"VALUES (%s,%s,%s)"
val = [id, name ,email]
mycursor.execute(sql, val)

mydb.commit()
mycursor.close()
print(mycursor.rowcount,"row counted")

)

id = input("enter the id")
name = input("enter the name")
email = input("enter the email")
insert(id, name, email)
