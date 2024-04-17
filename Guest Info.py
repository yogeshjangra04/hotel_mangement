import mysql.connector as sqlCon

myDB = sqlCon.connect(host = 'localhost', user = 'root', passwd = 'tetraacetyl', database = 'Hotel_Management')
if myDB.is_connected() == True:
    print("Successfully connected...")
else:
    print("Error in connection...")
cursor = myDB.cursor(buffered = True)

n = int(input("Enter no. of guests: "))
for i in range(n):
    gid = input("Enter guest ID: ")
    name = input("Enter guest name: ")
    gender = input("Enter guest gender: ")
    age = int(input("Enter age: "))
    city = input("Enter name of city: ")
    phone = input("Enter phone number: ")
    query = "INSERT INTO Guest VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(gid, name, gender, age, city, phone)
    cursor.execute(query)
myDB.commit()
myDB.close()
