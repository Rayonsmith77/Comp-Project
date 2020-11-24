import random 
import datetime 
file=open("guests.txt","a") 
file.write("Name\tPhone Number\tAddress\tCheck In\tCheck Out\tRoom Number\tCost") 

i = 0

# Home Function 
def Home():
        print("WELCOME TO HOTEL TRANSYLVANIA\n")
        print("1.Booking\n")
        print("2.Rooms Info\n")
        print("3.Payment\n")
        print("4.Record\n")
        print("0.Exit\n")

        ch=int(input("Enter your choice:"))

        if ch == 1:
                print(" ")
                Booking()

        elif ch == 2:
                print(" ")
                Rooms_Info()

        elif ch == 3:
                print(" ")
                Payment()

        elif ch == 4:
                print(" ")
                Record()

        elif ch == 0:
                exit()

        else:
                print("Invalid Choice")
                Home()
         

# Function to check validity of date used in Booking 

def date(c):
        if c[2] >= 2019 and c[2] <= 2020:
                if c[1] != 0 and c[1] <= 12:
                        if c[1] == 2 and c[0] != 0 and c[0] <= 31:
                                if c[2]%4 == 0 and c[0] <= 29:
                                        pass

                                elif c[0]<29:
                                        pass

                                else:
                                        print("Invalid date\n")
                                        name.pop(i)
                                        phno.pop(i)
                                        add.pop(i)
                                        checkin.pop(i)
                                        checkout.pop(i)
                                        Booking()
                        
                        
                        # If month is odd & less than equal to 7th month
                        elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
                                pass
                        
                        # If month is even & less than equal to 7th month and not 2nd month 
                        elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2: 
                                pass
                        
                        # If month is even & greater than equal to 8th month 
                        elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31: 
                                pass
                        
                        # If month is odd & greater than equal to 8th month
                        elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:
                                pass
                        
                        else: 
                                print("Invalid date\n") 
                                name.pop(i) 
                                phno.pop(i) 
                                add.pop(i) 
                                checkin.pop(i) 
                                checkout.pop(i) 
                                Booking() 
                                
                else: 
                        print("Invalid date\n") 
                        name.pop(i) 
                        phno.pop(i) 
                        add.pop(i) 
                        checkin.pop(i) 
                        checkout.pop(i) 
                        Booking()

        else: 
                print("Invalid date\n") 
                name.pop(i) 
                phno.pop(i) 
                add.pop(i) 
                checkin.pop(i) 
                checkout.pop(i) 
                Booking() 


# Function to Choose Room used in BOOKING

def Chooseroom():
                print()
                print("----SELECT ROOM TYPE----")
                print(" 1. Standard Non-AC")
                print(" 2. Standard AC")
                print(" 3. 3-Bed AC")
                print(" 4. Hotel Suite")
                print("Press 0 for Room Prices")
                print()
                ch=int(input("Choose your option:"))
                print()

                # If-conditions to display alloted room type and its price

                if ch==0:
                        print(" 1. Standard Non-AC - Rs. 3500")
                        print(" 2. Standard AC - Rs. 4000")
                        print(" 3. 3-Bed AC - Rs. 4500")
                        print(" 4. Hotel Suite - Rs. 6000")
                        ch=int(input("->"))

                if ch==1:
                        room.append('Standard Non-AC')
                        print("Room Type - Standard Non-AC")
                        price.append(3500)
                        print("Price - 3500")

                elif ch==2:
                        room.append('Standard AC')
                        print("Room Type - Standard AC")
                        price.append(4000)
                        print("Price - 4000")

                elif ch==3:
                        room.append('3-Bed Non-AC')
                        print("Room Type - 3-Bed Non-AC")
                        price.append(4500)
                        print("Price - 4500")

                elif ch==4:
                        room.append('Hotel Suite')
                        print("Room Type- Hotel Suite")
                        price.append(6000)
                        print("Price- 6000")

                else:
                        print(" Invalid Option")
                        Chooseroom()

                ch=input("Would you like to change your choice?(Y/N):")
                if ch in ["Y","y","Yes","yes","YES"]:
                        room.pop()
                        price.pop()
                        Chooseroom()


# Function to choose room no and customer ID used in BOOKING

def Roomno():
                print()
                print("Would you like to: \n 1.Choose your own room \n 2.Generate a random room")
                ch=int(input("->:"))
                if ch == 1:
                        while True:
                                rn=int(input("Enter room number(XXX):"))
                                cid=int(input("Enter your customer ID(XXX):"))
                                flag=0

                                if rn in roomno:
                                        print("Room number has been taken")
                                        flag=1
                                        
                                elif cid in custid:
                                        print("Customer ID has been taken")
                                        flag=1
                                        
                                if flag == 1:
                                        ch=int(input("Would you like to generate a random room number?:"))
                                        if ch == 2:
                                                break
                                break

                if ch == 2:
                        
                        # Randomly generating room no. and customer id for customer 
                        rn = random.randrange(40)+300
                        cid = random.randrange(40)+10

                        # Checks if alloted room no. & customer id already not alloted 
                        while rn in roomno or cid in custid: 

                                rn = random.randrange(60)+300
                                cid = random.randrange(60)+10
                        

                print("Alloted room number:",rn)
                print("Alloted Customer ID:",cid)

                ch = input("Would you like to change you Room No and Customer ID?(Y/N):")
                if ch in ["YES","yes","y","Y"]:
                        Roomno()

                return rn,cid
                
        

# BOOKING FUNCTION 
def Booking(): 
        
                # Used global keyword to use global variable 'i' 
                global i 
                print("BOOKING ROOMS") 
                print(" ") 
                
                while 1: 
                        n = str(input("Name:")) 
                        p1 = str(input("Phone No.:")) 
                        a = str(input("Address:")) 
                        
                        # Checks if any field is not empty 
                        if n!="" and p1!="" and a!="": 
                                name.append(n) 
                                add.append(a) 
                                break
                                
                        else: 
                                print("\tName, Phone no. & Address cannot be empty.") 
                        
                cii=str(input("Check-In(DD/MM/YYYY):")) 
                checkin.append(cii) 
                cii=cii.split('/') 
                ci=cii 
                ci[0]=int(ci[0]) 
                ci[1]=int(ci[1]) 
                ci[2]=int(ci[2]) 
                date(ci) 
                
                coo=str(input("Check-Out(DD/MM/YYYY):")) 
                checkout.append(coo) 
                coo=coo.split('/') 
                co=coo 
                co[0]=int(co[0]) 
                co[1]=int(co[1]) 
                co[2]=int(co[2]) 
                
                # Checks if check-out date falls after check-in date 
                if co[1]<ci[1] and co[2]<ci[2]: 
                        
                        print("\n\tError - Inconsistent Dates\n\tCheck-Out date must fall after Check-In\n") 
                        name.pop(i) 
                        add.pop(i) 
                        checkin.pop(i) 
                        checkout.pop(i) 
                        Booking() 
                elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]: 
                        
                        print("\n\tError - Inconsistent Dates\n\tCheck-Out date must fall after Check-In\n") 
                        name.pop(i) 
                        add.pop(i) 
                        checkin.pop(i) 
                        checkout.pop(i) 
                        Booking() 
                else: 
                        pass
                
                date(co) 
                d1 = datetime.datetime(ci[2],ci[1],ci[0]) 
                d2 = datetime.datetime(co[2],co[1],co[0]) 
                d = (d2-d1).days 
                day.append(d)

                Chooseroom()  # Function call for choosing room

                rn,cid=Roomno() # Function call for choosing room no and customer ID   
                
                         
                p.append(0) 
                                
                if p1 not in phno: 
                        phno.append(p1) 
                elif p1 in phno: 
                        for n in range(0,i): 
                                if p1== phno[n]: 
                                        if p[n]==1: 
                                                phno.append(p1) 
                elif p1 in phno: 
                        for n in range(0,i): 
                                if p1== phno[n]: 
                                        if p[n]==0: 
                                                print("\tPhone number exists but payment is not done") 
                                                name.pop(i) 
                                                add.pop(i) 
                                                checkin.pop(i) 
                                                checkout.pop(i) 
                                                Booking() 
                print("") 
                print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n") 
                print("Room No. - ",rn) 
                print("Customer Id - ",cid) 
                roomno.append(rn) 
                custid.append(cid) 
                i=i+1
                n=int(input("0-BACK\n ->")) 
                if n==0: 
                        Home() 
                else: 
                        exit() 

# ROOMS INFO 
def Rooms_Info(): 
        print("          ------ HOTEL ROOMS INFO ------") 
        print("") 
        print("STANDARD NON-AC") 
        print("---------------------------------------------------------------") 
        print("Room amenities include: 1 Double Bed, Television, Telephone,") 
        print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and") 
        print("an attached washroom with hot/cold water.\n") 
        print("STANDARD NON-AC") 
        print("---------------------------------------------------------------") 
        print("Room amenities include: 1 Double Bed, Television, Telephone,") 
        print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and") 
        print("an attached washroom with hot/cold water + Window/Split AC.\n") 
        print("3-Bed AC") 
        print("---------------------------------------------------------------") 
        print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,") 
        print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1") 
        print("Side table, Balcony with an Accent table with 2 Chair and an") 
        print("attached washroom with hot/cold water. Added Stocked minibar.\n") 
        print("Hotel Suite") 
        print("---------------------------------------------------------------") 
        print("Room amenities include: 1 King Size Bed, Flat Screen Television,") 
        print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ") 
        print("1 Side table, Balcony with an Accent table with 2 Chair and an") 
        print("attached washroom with hot/cold water + Window/Split AC.") 
        print("Added Stocked minibar\n")
        print()
        n=int(input("0-BACK\n ->")) 
        if n==0: 
                Home() 
        else: 
                exit() 

 
        
                                
# PAYMENT FUNCTION                       
def Payment(): 
        
        ph=str(input("Phone Number: ")) 
        global i 
        f=0
        
        for n in range(0,i): 
                if ph==phno[n] : 
                        
                        # Checks if payment is not already done 
                        if p[n]==0: 
                                f=1
                                totalcost=price[n]*day[n]
                                
                                print(" Payment")
                                print(" --------------------------------")
                                print(" MODE OF PAYMENT")
                                print(" 1- Credit/Debit Card")
                                print(" 2- Paytm/PhonePe")
                                print(" 3- Using UPI")
                                print(" 4- Cash")
                                x=int(input("-> "))
                                print("\n Amount: ",price[n]*day[n])
                                print("\n                Pay For Transylvania")
                                print(" (Yes/No)")
                                ch=str(input("->"))

                                if ch in ['Y','y','Yes','yes']: 
                                        
                                        print("\n\n --------------------------------")
                                        print("          Hotel Transylvania")
                                        print(" --------------------------------")
                                        print("                  Bill")
                                        print(" --------------------------------")
                                        print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
                                        print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
                                        print("\n Room Type: ",room[n],"\t\n Room Charges: ",price[n]*day[n],"\t")
                                        print(" --------------------------------")
                                        print("\n Total Amount: ",(price[n]*day[n]),"\t")
                                        print(" --------------------------------")
                                        print("          Thank You")
                                        print("          Visit Again :)")
                                        print(" --------------------------------\n")
                        
                                        file.write(name[n]+"\t"+str(phno[n])+"\t"+str(add[n])+"\t"+str(checkin[n])+"\t"+str(checkout[n])+"\t"+str(room[n])+"\t"+str(totalcost))
                                        p.pop(n)
                                        p.insert(n,1) 
                                        
                                        # pops room no. and customer id from list and 
                                        # later assigns zero at same position
                                        roomno.pop(n)
                                        custid.pop(n)
                                        roomno.insert(n,0)
                                        custid.insert(n,0) 
                                        
                        else:

                                for j in range(n+1,i): 
                                        if ph==phno[j] : 
                                                if p[j]==0: 
                                                        pass
                                                
                                                else: 
                                                        f=1
                                                        print("\n\tPayment has been Made :)\n\n") 
        if f==0:         
                print("Invalid Customer Id") 
                
        n = int(input("0-BACK\n ->")) 
        if n == 0: 
                Home() 
        else: 
                exit() 

# RECORD FUNCTION 
def Record(): 
        
        # Checks if any record exists or not 
        if phno!=[]: 
                print("  *** HOTEL RECORD ***\n") 
                print("| Name    | Phone No. | Address   | Check-In | Check-Out  | Room Type     | Price         |") 
                print("----------------------------------------------------------------------------------------------------------------------") 
                
                for n in range(0,i): 
                        print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",checkin[n],"\t|",checkout[n],"\t|",room[n],"\t|",price[n]) 
                
                print("----------------------------------------------------------------------------------------------------------------------") 
        
        else: 
                print("No Records Found") 
        n = int(input("0-BACK\n ->")) 
        if n == 0: 
                Home() 
                
        else: 
                exit()

# Global List Declaration 
name = [] 
phno = [] 
add = [] 
checkin = [] 
checkout = [] 
room = [] 
price = []  
p = [] 
roomno = [] 
custid = [] 
day = []

# Driver Code
Home() 
