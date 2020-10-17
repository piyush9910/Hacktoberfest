import datetime
import csv
def flight():
    with open('Flight.csv','r') as csvfile:
        data=csv.reader(csvfile)
        city1=input("City :")
        city2=input("Destination: ")
        year = int(input('Enter a year'))
        month = int(input('Enter a month'))
        day = int(input('Enter a day'))
        hour=int(input("Enter Hour"))
        minute=int(input("Enter Minute"))
        date1=datetime.datetime(year, month, day, hour, minute)
        if hour>12:
            charge=1203

        for i in data:
            if city1==i[0] and city2==i[1]==city2:
                fare=int(i[2])*0.018+int(i[2])+charge
                print("Total price is : ",fare,"including 18% GST.", "for Date ",date1)
flight()