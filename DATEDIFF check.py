import mysql.connector as sqlCon

myDB = sqlCon.connect(host = 'localhost', user = 'root', passwd = 'tetraacetyl', database = 'Hotel_Management')
if myDB.is_connected() == True:
    print("Successfully connected...")
else:
    print("Error in connection...")
cursor = myDB.cursor(buffered = True)
rn = int(input("Enter room no: "))
query = 'SELECT room_rent FROM room WHERE room_number = {}'.format(rn)
cursor.execute(query)
records = cursor.fetchall()
print(int(records[0][0][2:])*10)
