import random
import csv
import datetime
print("\t\t\t\tHello and Welcome To Hotel Maintained By Python Server........\n")
name=input("Your Good Name  : \n")
phoneno=int(input("Enter Your Phone_Number\n "))
orderid=random.randint(11,999999999)
list1=[]

def hoteldelhi():
    print("\t1. Central Delhi")
    print("\t2. Gurugram")
    print("\t3. Noida")
    c=int(input("Enter Your Choice : "))
    if c==1:
        print("Central Delhi")
        with open('Hotel1.csv', 'r') as csv_file:
            read = csv.reader(csv_file)
            print('S.no\tName \tPrice')
            for i in read:
                print(i[1] + '\t\t' + i[0], i[2])
            n = int(input("How Many Types of Rooms"))
            for i in range(n):
                nn = int(input("Enter Your Choice"))
                if nn == 1:
                    price = 1500
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 2:
                    price = 1900
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 3:
                    price = 2500
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 4:
                    price = 3000
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                else:
                    print("INVALID ENTRY")
    elif c==2:
        print("Gurugram")
        with open('Hotel2.csv', 'r') as csv_file:
            read = csv.reader(csv_file)
            print('S.no\tName \tPrice')
            for i in read:
                print(i[1] + '\t\t' + i[0], i[2])
            n = int(input("How Many Types of Rooms"))
            for i in range(n):
                nn = int(input("Enter Your Choice"))
                if nn == 1:
                    price = 1400
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 2:
                    price = 1800
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 3:
                    price = 2400
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 4:
                    price = 2900
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                else:
                    print("INVALID ENTRY")
    elif c==3:
        print("Noida")
        with open('Hotel3.csv', 'r') as csv_file:
            read = csv.reader(csv_file)
            print('S.no\tName \tPrice')
            for i in read:
                print(i[1] + '\t\t' + i[0], i[2])
            n = int(input("How Many Types of Rooms"))
            for i in range(n):
                nn = int(input("Enter Your Choice"))
                if nn == 1:
                    price = 1300
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 2:
                    price = 1700
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 3:
                    price = 2300
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 4:
                    price = 2800
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                else:
                    print("INVALID ENTRY")


def hotelmumbai():
    print("\t1. Bandra")
    print("\t2. Navi-Mumbai")
    print("\t3. Nashik")
    c=int(input("Enter Your Choice : "))
    if c==1:
        print("Bandra")
        with open('Hotel1.csv', 'r') as csv_file:
            read = csv.reader(csv_file)
            print('S.no\tName \tPrice')
            for i in read:
                print(i[1] + '\t\t' + i[0], i[2])
            n = int(input("How Many Types of Rooms"))
            for i in range(n):
                nn = int(input("Enter Your Choice"))
                if nn == 1:
                    price = 1500
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 2:
                    price = 1900
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 3:
                    price = 2500
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 4:
                    price = 3000
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                else:
                    print("INVALID ENTRY")
    elif c==2:
        print("Navi Mumbai")
        with open('Hotel2.csv', 'r') as csv_file:
            read = csv.reader(csv_file)
            print('S.no\tName \tPrice')
            for i in read:
                print(i[1] + '\t\t' + i[0], i[2])
            n = int(input("How Many Types of Rooms"))
            for i in range(n):
                nn = int(input("Enter Your Choice"))
                if nn == 1:
                    price = 1400
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 2:
                    price = 1800
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 3:
                    price = 2400
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 4:
                    price = 2900
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                else:
                    print("INVALID ENTRY")
    elif c==3:
        print("Nashik")
        with open('Hotel3.csv', 'r') as csv_file:
            read = csv.reader(csv_file)
            print('S.no\tName \tPrice')
            for i in read:
                print(i[1] + '\t\t' + i[0], i[2])
            n = int(input("How Many Types of Rooms"))
            for i in range(n):
                nn = int(input("Enter Your Choice"))
                if nn == 1:
                    price = 1300
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 2:
                    price = 1700
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 3:
                    price = 2300
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 4:
                    price = 2800
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                else:
                    print("INVALID ENTRY")



def hotelbangalore():
    print("\t1. Central Delhi")
    print("\t2. Gurugram")
    print("\t3. Noida")
    c=int(input("Enter Your Choice : "))
    if c==1:
        print("Central Delhi")
        with open('Hotel1.csv', 'r') as csv_file:
            read = csv.reader(csv_file)
            print('S.no\tName \tPrice')
            for i in read:
                print(i[1] + '\t\t' + i[0], i[2])
            n = int(input("How Many Types of Rooms"))
            for i in range(n):
                nn = int(input("Enter Your Choice"))
                if nn == 1:
                    price = 1500
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 2:
                    price = 1900
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 3:
                    price = 2500
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 4:
                    price = 3000
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                else:
                    print("INVALID ENTRY")
    elif c==2:
        print("Gurugram")
        with open('Hotel2.csv', 'r') as csv_file:
            read = csv.reader(csv_file)
            print('S.no\tName \tPrice')
            for i in read:
                print(i[1] + '\t\t' + i[0], i[2])
            n = int(input("How Many Types of Rooms"))
            for i in range(n):
                nn = int(input("Enter Your Choice"))
                if nn == 1:
                    price = 1400
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 2:
                    price = 1800
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 3:
                    price = 2400
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 4:
                    price = 2900
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                else:
                    print("INVALID ENTRY")
    elif c==3:
        print("Noida")
        with open('Hotel3.csv', 'r') as csv_file:
            read = csv.reader(csv_file)
            print('S.no\tName \tPrice')
            for i in read:
                print(i[1] + '\t\t' + i[0], i[2])
            n = int(input("How Many Types of Rooms"))
            for i in range(n):
                nn = int(input("Enter Your Choice"))
                if nn == 1:
                    price = 1300
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 2:
                    price = 1700
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 3:
                    price = 2300
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                elif nn == 4:
                    price = 2800
                    q = int(input("No of Days: "))
                    t = price * q
                    list1.append(t)

                else:
                    print("INVALID ENTRY")


def bill(name,phoneno):
    print("\t" * 10 + "Total Food Bill\n")
    print("*" * 80)
    print()
    e = datetime.datetime.now()
    print("Date :                       ",e.strftime("%Y-%m-%d %H:%M:%S"))
    print()
    print("Customer Name :              ", name)
    print("OrderId :                    ", orderid)
    print("PhoneNo :                    ", phoneno)
    print("*" * 80)
    s = sum(list1)
    print("Total Billing Amount :                  ", s.__round__())
    print("*" * 80)
    print("Thankyou , Come Visit Again......")
    print()
    print("You will receive and sms for your valuable Feedback. You can Give reviews on our website too...")


def mainmenu():
    print("\t\t\tYou Can Choose from the Below Options(Hotel Booking)")
    print()
    print("\t\t1. Delhi ")
    print()
    print("\t\t2. Mumbai ")
    print()
    print("\t\t3. Bangalore ")
    print()
    print("\t\t4. Bill")
    print()
    ch=int(input("Enter Your Choice : "))
    if ch==1:
        hoteldelhi()
    elif ch==2:
        hotelmumbai()
    elif ch==3:
        hotelbangalore()
    elif ch==4:
        bill(name,phoneno)
    else:
        print("INVALID ")
    inp=input("Do you want to Continue : (Y/N)")
    if inp=='Y' or inp=='y':
        mainmenu()
    else:
        bill(name,phoneno)


mainmenu()


