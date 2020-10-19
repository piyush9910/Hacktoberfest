import random
import csv
import datetime

print("\t\t\t\tHello and Welcome To Restraunt Maintained By Python Server........\n")
name=input("Your Good Name  : \n")
phoneno=int(input("Enter Your Phone_Number\n "))
orderid=random.randint(1111111,999999999)
list1=[]

#here are the funcyions for each food menu
def food():
    with open('Food.csv', 'r') as csv_file:
        read = csv.reader(csv_file)
        print('S.no\tName \tPrice')
        for i in read:
            print(i[1] + '\t\t' + i[0], i[2])
        n = int(input("How Many Items you want to Order"))
        for i in range(n):
            nn = int(input("Enter Your Choice"))
            if nn == 1:

                price = 35.50
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 2:
                price = 50.40
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 3:
                price = 45.80
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 4:
                price = 50.60
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 5:
                price = 45.50
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 6:
                price = 37.30
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 7:
                price = 51.80
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 8:
                price = 35.90
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 9:
                price = 43.50
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 10:
                price = 37.50
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            else:
                print("INVALID ENTRY")


def snacks():
    with open('Snacks.csv', 'r') as csv_file:
        read = csv.reader(csv_file)
        print('S.no\tName \tPrice')
        for i in read:
            print(i[1] + '\t\t' + i[0], i[2])
        n = int(input("How Many Items you want to Order"))
        for i in range(n):
            nn = int(input("Enter Your Choice"))
            if nn == 1:
                price = 35.50
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 2:
                price = 50.40
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 3:
                price = 45.80
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 4:
                price = 50.60
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 5:
                price = 45.50
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            else:
                print("INVALID ENTRY")


def drinks():
    with open('Drinks.csv', 'r') as csv_file:
        read = csv.reader(csv_file)
        print('S.no\tName \tPrice')
        for i in read:
            print(i[1] + '\t\t' + i[0], i[2])
        n = int(input("How Many Items you want to Order"))
        for i in range(n):
            nn = int(input("Enter Your Choice"))
            if nn == 1:
                price = 35.50
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 2:
                price = 50.40
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 3:
                price = 45.80
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 4:
                price = 50.60
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 5:
                price = 45.50
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 6:
                price = 37.30
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 7:
                price = 51.80
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 8:
                price = 35.90
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 9:
                price = 43.50
                q = int(input("Enter Your Quantity"))
                t = price * q
                list1.append(t)

            elif nn == 10:
                price = 37.50
                q = int(input("Enter Your Quantity"))
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
    exit()


def reg():
    print(".... Registeration ....")
    email=input("Enter your Email ID : ")
    passwd=input("Choose a Password : ")
    with open('Password.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow([email,passwd])
        print("Account Succesfully Created ...")
    print("Login Using Your Email id and Password.")
    print("")
    login()

def login():
    print("Login...")
    login = False

    while login == False:
        data = []
        with open("Password.csv") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        #print(data)
        un = input("Username : ")
        pw = input("Password : ")
        col0 = [x[0] for x in data]
        col1 = [x[1] for x in data]

        if un in col0:

            for k in range(0, len(col0)):
                if col0[k] == un and col1[k] == pw:
                    print("Login Succesfull")
                    login = True
                    menu()
        else:
            print("Wrong Password")





def mainmenu():
    print("\t\t\tYou Can Choose from the Below Options")
    print()
    print("\t\t1. New User")
    print()
    print("\t\t2. Existing User")
    print()
    c=int(input("Enter your Choice : "))
    if c==1:
        print("Registeration")
        reg()
    elif c==2:
        login()
    else:print("INVALID ...")

def menu():
    print("\t\t1. Food Menu ")
    print()
    print("\t\t2. Beverages Menu ")
    print()
    print("\t\t3. Snacks ")
    print()
    print("\t\t4. Bill")
    print()
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        food()
    elif ch == 2:
        drinks()
    elif ch == 3:
        snacks()
    elif ch == 4:
        bill(name, phoneno)
    else:
        print("INVALID ")
    inp = input("Do you want to Continue : (Y/N)")
    if inp == 'Y' or inp == 'y':
        menu()
    else:
        bill(name, phoneno)

mainmenu()
