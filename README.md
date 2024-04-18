# Hotel-Management
![python](http://ForTheBadge.com/images/badges/made-with-python.svg)

Hotel Management System using Python and MySQL as a backend database

# Main Features
### Opening screen
```hotel
                                                 WELCOME TO HOTEL Atlante Plaza

                         1 Rooms Info

                         2 Guest Info

                         3 Booking Info

                         4 Add Room

                         5 Add Guest

                         6 Add Booking

                         7 Delete Booking

                         8 Edit Guest

                         9 Available Date Search

                         10 Report Generation

                         0 Exit
```
# Room Info
Displays room number, type, accommodation, rent.

```room
Room_Number              Floor_Number             Room_Type                Room_Accommodation       Room_Rent


101                      1                        Villa Suite              5                        $ 1251

102                      1                        Deluxe AC(Triple)        3                        $ 1024

103                      1                        Deluxe AC(Double)        2                        $ 932

104                      1                        Deluxe AC(Triple)        3                        $ 1024

105                      1                        Deluxe AC(Quad)          4                        $ 1116

106                      1                        Standard Non-AC(Quad)    4                        $ 972

107                      1                        Deluxe Non-AC(Quad)      4                        $ 1116

108                      1                        Deluxe Non-AC(Triple)    3                        $ 1024

109                      1                        Deluxe AC(Single)        1                        $ 840

110                      1                        Deluxe Non-AC(Double)    2                        $ 932

111                      1                        Deluxe AC(Single)        1                        $ 840

112                      1                        Villa Suite              5                        $ 1251

113                      1                        Deluxe Non-AC(Single)    1                        $ 840

114                      1                        Standard Non-AC(Single)  1                        $ 696

115                      1                        Standard AC(Single)      1                        $ 712

116                      1                        Master Suite             5                        $ 1064

117                      1                        Deluxe AC(Double)        2                        $ 932

118                      1                        Standard Non-AC(Quad)    4                        $ 972

119                      1                        Villa Suite              5                        $ 1251

```

# Guest Info
Displays guest information like name, gender, age etc.

<b>Disclaimer</b>: Data that has been used here is fictitious and not meant to be taken seriously.

```guest
G118                 Ritesh Das           M                    18                   Kolkata, India       +91 7777777777

G119                 John Hopkins         M                    32                   Miami, USA           +1 9123491234

G120                 Bethany McCallister  F                    24                   Los Angeles, USA     +1 8777787777

G121                 Leonardo DiCaprio    M                    48                   Los Angeles, USA     +1 6444464444

G122                 Luis Suarez          M                    35                   Montevideo, Uruguay  +598 6111161111        

G123                 Disha Patani         F                    30                   Mumbai, India        +91 8333383333

G124                 James Rodriguez      M                    38                   Cucuta, Colombia     +57 3000030000

G125                 Edison Da Silva      M                    72                   Rio De Janeiro, Brazil +55 5432154321       

G126                 Cristiano Ronaldo    M                    37                   Lisbon, Portugal     +351 6222262222        

G127                 Bernardo Silva       M                    28                   Lisbon, Portugal     +351 7666676666        

G128                 Mohammed Salisu      M                    23                   Accra, Ghana         +233 7999979999        

G129                 Gary McCoy           M                    50                   Sydney, Australia    +61 5987659876

G130                 Dominik Livakovic    M                    27                   Zadar, Croatia       +385 7111171111
```
# Booking Info
Displays booking information like check-in check-out dates, room number, total cost etc.

```booking
BookingID        GuestID          Room_Number      Floor_Number     check_in         check_out        total_amt       


B001             G118             207              2                2022-10-01       2022-10-09       $ 8960

B002             G124             209              2                2022-12-10       2022-12-23       $ 16912

B004             G122             710              7                2022-12-15       2022-12-29       $ 13200

B005             G119             105              1                2022-12-03       2022-12-19       $ 18972

B006             G131             917              9                2022-12-07       2022-12-13       $ 7812

B007             G125             511              5                2022-12-02       2022-12-25       $ 24576

B009             G117             503              5                2022-12-09       2022-12-24       $ 11392

B010             G126             112              1                2022-12-03       2022-12-26       $ 30024
```

# Edit Guest
```editguest
What do you want to update/modify?
                         1 Name

                         2 Gender

                         3 Age

                         4 City

                         5 Phone

->3
Enter your GuestID: G137
Enter new age: 34
Changes made successfully...
```

# Available Date Search
Checks whether a particular room has been assigned to a guest or not.
```datesearch
Enter room no. 207
Enter floor no. 2


Room_Number     Floor_Number    check_in        check_out
207             2               2022-10-01      2022-10-09


207             2               2022-12-17      2022-12-29
```
# Report Generation
Generates reports based on booking status, community, room types and rents.
```report
->1
                         1 Booking Status & Personal Details

                         2 Guest Details From a Particular City

                         3 Room Types and Rents

->1
Enter your BookingID: B001
BookingID        GuestID          Room_Number      Floor_Number     check_in         check_out        total_amt       
B001             G118             207              2                2022-10-01       2022-10-09       $ 8960

GuestID              Name                 Gender               Age                  City                 Phone
G118                 Ritesh Das           M                    18                   Kolkata, India       +91 7980369670

->2
Enter name of city: Kolkata, India

GuestID              Name                 Gender               Age                  City                 Phone


G118                 Ritesh Das           M                    18                   Kolkata, India       +91 7777777777

G132                 Boibaswata Chakraborty M                    17                   Kolkata, India       +91 9654396543       

G133                 Shreyash Chanda      M                    18                   Kolkata, India       +91 9012390123

->3
Room_Type                Room_Rent

Deluxe AC(Double)        $ 932

Deluxe AC(Quad)          $ 1116

Deluxe AC(Single)        $ 840

Deluxe AC(Triple)        $ 1024

Deluxe Non-AC(Double)    $ 932

Deluxe Non-AC(Quad)      $ 1116

Deluxe Non-AC(Single)    $ 840

Deluxe Non-AC(Triple)    $ 1024
```


