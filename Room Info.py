import random
rt = ['Standard AC(Single)', 'Standard Non-AC(Single)', 'Deluxe AC(Single)', 'Deluxe Non-AC(Single)',
      'Standard AC(Double)', 'Standard Non-AC(Double)', 'Deluxe AC(Double)', 'Deluxe Non-AC(Double)',
      'Standard AC(Triple)', 'Standard Non-AC(Triple)', 'Deluxe AC(Triple)', 'Deluxe Non-AC(Triple)',
      'Standard AC(Quad)', 'Standard Non-AC(Quad)', 'Deluxe AC(Quad)', 'Deluxe Non-AC(Quad)',
      'Mini Suite', 'Master Suite', 'Executive Suite', 'Presidential Room', 'Penthouse Suite', 'Villa Suite']
      
      
import mysql.connector as sqlCon
myDB = sqlCon.connect(host = 'localhost', user = 'root', passwd = 'tetraacetyl', database = 'Hotel_Management')
if myDB.is_connected() == True:
    print("Successfully connected...")
else:
    print("Error in connection...")
cursor = myDB.cursor(buffered = True)
for i in range(1, 12):
    for j in range(1, 20):
        ra = 0
        rr = 0
        rn = i*100+j
        fn = i
        x = random.randint(0, len(rt)-1)
        RT = rt[x]
        if x in [0, 1, 2, 3]:
            ra = 1
        elif x in [4, 5, 6, 7]:
            ra = 2
        elif x in [8, 9, 10, 11]:
            ra = 3
        elif x in [12, 13, 14, 15]:
            ra = 4
        elif x in [16, 17, 18, 19]:
            ra = 5
        else:
            ra = 5

        if x in [0, 4, 8, 12, 16]:
            rr = '$' + str(712 + 23*x)
        elif x in [1, 5, 9, 13, 17]:
            rr = '$' + str(673 + 23*x)
        elif x in [2, 6, 10, 14, 18]:
            rr = '$' + str(794 + 23*x)
        elif x in [3, 7, 11, 15, 19]:
            rr = '$' + str(771 + 23*x)
        else:
            rr = '$1251'
        query = "INSERT INTO Room VALUES ('{}', '{}', '{}', '{}', '{}')".format(rn, fn, RT, ra, rr)
        cursor.execute(query)
myDB.commit()
myDB.close()


            
        
