import mysql.connector as sqlCon

myDB = sqlCon.connect(host = 'localhost', user = 'root', passwd = 'tetraacetyl', database = 'Hotel_Management')
if myDB.is_connected() == True:
    print("Successfully connected...")
else:
    print("Error in connection...")
cursor = myDB.cursor(buffered = True)

n = int(input("Enter no. of bookings: "))
for i in range(n):
    bid = input("Enter booking ID: ")
    gid = input("Enter guest ID: ")
    rn = int(input("Enter room no. "))
    fn = int(input("Enter floor no. "))
    checkin = input("Enter booking start date: ")
    checkout = input("Enter booking end date: ")
    day = int(input("Enter no. of days: "))
    query = 'SELECT room_rent FROM room WHERE room_number = {}'.format(rn)
    cursor.execute(query)
    records = cursor.fetchall()
    total_amt = '$ ' + str(int(records[0][0][2:])*day)
    query = "INSERT INTO booking VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(bid, gid, rn, fn, checkin, checkout, total_amt)
    cursor.execute(query)
myDB.commit()
myDB.close()
