import csv
login=False

while login==False:
   data=[]
   with open("Password.csv") as csvfile:
      reader=csv.reader(csvfile)
      for row in reader:
         data.append(row)
   print(data)
   un=input("Username : ")
   pw=input("Password : ")
   col0 = [x[0] for x in data]
   col1 = [x[1] for x in data]

   if un in col0:

      for k in range(0, len(col0)):
         if col0[k]==un and col1[k]==pw:
            print("Login Succesfull")
            login=True
   else:
      print("Wrong Password")
