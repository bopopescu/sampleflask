import mysql.connector

cnx = mysql.connector.connect(user='root', password='rootroot', database='sample')
cursor = cnx.cursor()

query = "SELECT id,name,phone,email FROM std"

cursor.execute(query)

for (id, name, phone, email) in cursor:
    print(id,name,phone,email)

cursor.close()
cnx.close()
