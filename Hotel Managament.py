import mysql.connector as sqlCon
myHotel = sqlCon.connect(host = 'localhost', user = 'root', passwd = '', database = 'Hotel_Management')
if myHotel.is_connected() == True:
    print(" ")
    print("\t\t\t\t\t\t WELCOME TO HOTEL Atlante Plaza\n")
else:
    print("Error in connection...")
    
cursor = myHotel.cursor(buffered = True)

def Hotel():
    print("\t\t\t 1 Rooms Info\n")
    print("\t\t\t 2 Guest Info\n")
    print("\t\t\t 3 Booking Info\n")
    print("\t\t\t 4 Add Room\n")
    print("\t\t\t 5 Add Guest\n")
    print("\t\t\t 6 Add Booking\n")
    print("\t\t\t 7 Delete Booking\n")
    print("\t\t\t 8 Edit Guest\n")
    print("\t\t\t 9 Available Date Search\n")
    print("\t\t\t 10 Report Generation\n")
    print("\t\t\t 0 Exit\n")

    try:
        ch=int(input("->"))
    
        if ch == 1:
            print('\n')
            Rooms_Info()
        
        elif ch == 2:
            print(" ")
            Guest_Info()
        
        elif ch == 3:
            print(" ")
            Booking_Info()
        
        elif ch == 4:
            print(" ")
            while True:
                try:
                    Add_Room()
                    break
                except:
                    print("Please enter details properly.")
                    print('\n')
        
        elif ch == 5:
            print(" ")
            while True:
                try:
                    Add_Guest()
                    break
                except:
                    print("Please enter details properly.")
                    print('\n')
        
        elif ch == 6:
            print(" ")
            while True:
                try:
                    Add_Booking()
                    break
                except:
                    print("Please enter details properly.")
                    print('\n')

        elif ch == 7:
            print(" ")
            Delete_Booking()

        elif ch == 8:
            print(" ")
            while True:
                try:
                    Edit_Guest()
                    break
                except:
                    print("Please enter details properly.")
                    print('\n')

        elif ch == 9:
            print(" ")
            while True:
                try:
                    Available_Date_Search()
                    break
                except:
                    print("Please enter details properly.")
                    print('\n')

        elif ch == 10:
            print(" ")
            Report_Generation()

        elif ch == 0:
            exit()

    except:
        print("Please enter a valid number between 0 to 10.")
        print('\n')

def Rooms_Info():
    cursor.execute("SELECT * FROM Room")
    data = cursor.fetchall()
    records = []
    columns = cursor.description
    
    for record in columns:
        records.append(record[0])
        
    print('{:<24} {:<24} {:<24} {:<24} {:<24}'.format(*records))
    print('\n')
    
    for record in data:
        print('{:<24} {:<24} {:<24} {:<24} {:<24}'.format(*record))
        print('\t')

def Guest_Info():
    cursor.execute("SELECT * FROM Guest")
    data = cursor.fetchall()
    records = []
    columns = cursor.description
    
    for record in columns:
        records.append(record[0])
        
    print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(*records))
    print('\n')
    
    for record in data:
        print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(*record))
        print('\t')

def Booking_Info():
    cursor.execute("SELECT * FROM Booking")
    data = cursor.fetchall()
    records = []
    columns = cursor.description
    
    for record in columns:
        records.append(record[0])
        
    print('{:<16} {:<16} {:<16} {:<16} {:<16} {:<16} {:<16}'.format(*records))
    print('\n')
    
    for record in data:
        record = list(record)
        for i in range(len(record)):
            record[i] = str(record[i])
            
        print('{:<16} {:<16} {:<16} {:<16} {:<16} {:<16} {:<16}'.format(*record))
        print('\t')
        
def Room_Availability(RN, DateIn, DateOut):
    room_available = True
    room_booked = False
    cursor.execute("SELECT Room_Number FROM Booking")
    data = cursor.fetchall()
    
    for record in data:
        if RN in record:
            room_available = False

    if room_available == False:
        cursor.execute("SELECT check_out FROM Booking WHERE Room_Number = {}".format(RN))
        data = cursor.fetchall()
        booking_end_date = str(data[0][0])
        
        cursor.execute("SELECT check_in FROM Booking WHERE Room_Number = {}".format(RN))
        data = cursor.fetchall()
        booking_start_date = str(data[0][0])

        if (DateIn>=booking_start_date and DateIn<=booking_end_date) or (DateOut>=booking_start_date and DateOut<=booking_end_date):
            room_booked = True

        if room_booked and not(room_available):
            return False
        else:
            return True
    else:
        return True

def Add_Room():
    RN = int(input("Enter room no. "))
    FN = int(input("Enter floor no. "))
    RT = input("Enter room type: ")
    RA = int(input("Enter room accommodation: "))
    RR = input("Enter room rent: ")
    Rquery = "INSERT INTO Room VALUES ('{}', '{}', '{}', '{}', '{}')".format(RN, FN, RT, RA, RR)
    cursor.execute(Rquery)
    myHotel.commit()
    print("Room details were added successfully.\n")


def Add_Guest():
    cursor.execute("SELECT max(GuestID) FROM Guest")
    data = cursor.fetchall()
    GID_old = data[0][0]
    GID_old_num = int(GID_old[1:])
    GID_new = 'G' + str(GID_old_num + 1)
    name = input("Enter your name: ")
    gender = input("Enter your gender: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    phone = input("Enter your phone no. ")
    Gquery = "INSERT INTO Guest VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(GID_new, name, gender, age, city, phone)
    cursor.execute(Gquery)
    myHotel.commit()
    print("Guest details were added successfully.\n")

def Date_Diff(DateIn, DateOut):
    query = "SELECT DATEDIFF('{}', '{}')".format(DateOut, DateIn)
    cursor.execute(query)
    data = cursor.fetchall()
    Diff = data[0][0] + 1
    return Diff

def Room_Rent(RN):
    query = "SELECT Room_Rent FROM Room WHERE Room_Number = '{}'".format(RN)
    cursor.execute(query)
    data = cursor.fetchall()
    Rent = int(data[0][0][2:])
    return Rent
 
def Add_Booking():
    cursor.execute("SELECT max(BookingID) FROM Booking")
    data = cursor.fetchall()
    BID_old = data[0][0]
    BID_old_num = int(BID_old[1:])
    
    if len(str(BID_old_num)) == 1:
        BID_new = 'B00' + str(BID_old_num + 1)
    elif len(str(BID_old_num)) == 2:
        BID_new = 'B0' + str(BID_old_num + 1)
    else:
        BID_new = 'B' + str(BID_old_num + 1)

    GID = input("Enter your GuestID: ")
    RN = int(input("Enter your Room No. "))
    FN = int(input("Enter your Floor No. "))
    DateIn = input("Enter your booking start date: ")
    DateOut = input("Enter your booking end date: ")
    total_amt = '$ ' + str(Room_Rent(RN)*Date_Diff(DateIn, DateOut))
    
    if Room_Availability(RN, DateIn, DateOut) == True:
        Bquery = "INSERT INTO booking VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(BID_new, GID, RN, FN, DateIn, DateOut, total_amt)
        cursor.execute(Bquery)
        myHotel.commit()
        print("Your booking was successful. Please check your e-mail for a booking confirmation. We'll see you soon!")
    else:
        print("Sorry, we weren't able to provide you a room with the aforesaid details. Please try again later.")

def Delete_Booking():
    present = False
    while True:
        BID = input("Enter your BookingID: ")
        Bquery = "SELECT BookingID FROM Booking"
        cursor.execute(Bquery)
        data = cursor.fetchall()
        for record in data:
            if BID == record[0]:
                present = True
        if present:
            Dquery = "DELETE FROM Booking WHERE BookingID = '{}'".format(BID)
            cursor.execute(Dquery)
            myHotel.commit()
            print("Booking was cancelled successfully.")
            break
        else:
            print("Please enter a valid bookingID.\n")
        
def Edit_Guest():
    print("What do you want to update/modify?")
    print("\t\t\t 1 Name\n")
    print("\t\t\t 2 Gender\n")
    print("\t\t\t 3 Age\n")
    print("\t\t\t 4 City\n")
    print("\t\t\t 5 Phone\n")
    ch = int(input("->"))
    GID = input("Enter your GuestID: ")
    
    if ch == 1:
        name = input("Enter new name: ")
        Nquery = "UPDATE Guest SET Name = '{}' WHERE GuestID = '{}'".format(name, GID)
        cursor.execute(Nquery)
        myHotel.commit()
        print("Changes made successfully...")
        
    elif ch == 2:
        gender = input("Enter new gender: ")
        Nquery = "UPDATE Guest SET Gender = '{}' WHERE GuestID = '{}'".format(gender, GID)
        cursor.execute(Nquery)
        myHotel.commit()
        print("Changes made successfully...")

    elif ch == 3:
        age = int(input("Enter new age: "))
        Nquery = "UPDATE Guest SET Age = {} WHERE GuestID = '{}'".format(age, GID)
        cursor.execute(Nquery)
        myHotel.commit()
        print("Changes made successfully...")

    elif ch == 4:
        city = input("Enter new city: ")
        Nquery = "UPDATE Guest SET City = '{}' WHERE GuestID = '{}'".format(city, GID)
        cursor.execute(Nquery)
        myHotel.commit()
        print("Changes made successfully...")

    elif ch == 5:
        phone = input("Enter new phone no. ")
        Nquery = "UPDATE Guest SET phone = '{}' WHERE GuestID = '{}'".format(phone, GID)
        cursor.execute(Nquery)
        myHotel.commit()
        print("Changes made successfully...")
        

def Available_Date_Search():
    RN = int(input("Enter room no. "))
    FN = int(input("Enter floor no. "))
    Rquery = "SELECT Room_Number FROM Booking"
    cursor.execute(Rquery)
    data = cursor.fetchall()
    print('\n')
    
    for record in data:
        if RN in record:
            Dquery = "SELECT Room_Number, Floor_Number, check_in, check_out FROM Booking WHERE Room_Number = {} AND Floor_Number = {}".format(RN, FN)
            cursor.execute(Dquery)
            data = cursor.fetchall()
            columns = cursor.description
            
            for record in columns:
                print(record[0], end = '\t')
            print('\t')
            
            for record in data:
                for eL in record[:-2]:
                    print(eL, end = '\t\t')
                print(str(record[-2]) + '\t' + str(record[-1]))
                print('\n')
            break
    else:
        Dquery = "SELECT Room_Number, Floor_Number, check_in, check_out FROM Booking"
        cursor.execute(Dquery)
        columns = cursor.description
        
        for record in columns:
            print(record[0], end = '\t')
        print('\t')
        print(str(RN) + '\t\t' + str(FN) + '\t\tNot yet booked\tNot yet booked\n')

def Report_Generation():
    print('\t\t\t 1 Booking Status & Personal Details\n')
    print('\t\t\t 2 Guest Details From a Particular City\n')
    print('\t\t\t 3 Room Types and Rents\n')
    ch = int(input('->'))
    
    if ch == 1:
             
        while True:
            present = False
            BID = input("Enter your BookingID: ")
            Bquery = "SELECT BookingID FROM Booking"
            cursor.execute(Bquery)
            data = cursor.fetchall()
            for record in data:
                if BID == record[0]:
                    present = True
            if present:
                Bquery = "SELECT * FROM Booking WHERE BookingID = '{}'".format(BID)
                cursor.execute(Bquery)
                data = cursor.fetchall()
                columns = cursor.description
                records = []
                
                for record in columns:
                    records.append(record[0])
                print('{:<16} {:<16} {:<16} {:<16} {:<16} {:<16} {:<16}'.format(*records))
                
                for record in data:
                    record = list(record)
                    for i in range(len(record)):
                        record[i] = str(record[i])
                    print('{:<16} {:<16} {:<16} {:<16} {:<16} {:<16} {:<16}'.format(*record))
                print('\t')
                
                GBquery = "SELECT Guest.GuestID, Name, Gender, Age, City, Phone FROM Guest, Booking WHERE Guest.GuestID = Booking.GuestID AND BookingID = '{}'".format(BID)
                cursor.execute(GBquery)
                data = cursor.fetchall()
                records = []
                columns = cursor.description
                
                for record in columns:
                    records.append(record[0])
                print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(*records))
                
                for record in data:
                    print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(*record))
                    print('\t')
                print('\n')
                break
            else:
                print("Please enter a valid bookingID.\n")

    elif ch == 2:
        City = input("Enter name of city: ")
        print('\t')
        Cquery = "SELECT * FROM Guest WHERE City = '{}'".format(City)
        cursor.execute(Cquery)
        data = cursor.fetchall()
        records = []
        columns = cursor.description
        
        for record in columns:
            records.append(record[0])
            
        print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(*records))
        print('\n')
        
        for record in data:
            print('{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(*record))
            print('\t')
        print('\n')

    elif ch == 3:
        print('\t')
        cursor.execute("SELECT DISTINCT Room_Type, Room_Rent FROM Room ORDER BY Room_Type")
        data = cursor.fetchall()
        records = []
        columns = cursor.description
        
        for record in columns:
            records.append(record[0])
        print('{:<24} {:<24}'.format(*records))
        print('\t')
        
        for record in data:
            print('{:<24} {:<24}'.format(*record))
        print('\n')

while True:
    Hotel()
    
