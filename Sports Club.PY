import os
import platform
import mysql.connector
import pandas as pd

mydb=mysql.connector.connect(host="localhost",\
user="root",\
passwd="#mrverma1489",\
database="sports")
mycursor=mydb.cursor()
def RegisterClub():
  L=[]
  enroll=int(input("Enter the registration number(Max 5 Digits) : "))
  L.append(enroll)
  sname=input("Enter the Name of club member: ")
  L.append(sname)
  age=int(input("Enter Age of member : "))
  L.append(age)
  city=input("Enter the City of the member : ")
  L.append(city)
  sportname=input("Enter the sportname : ")
  L.append(sportname)
  phone=input("Enter Phone number in Digits : ")
  L.append(phone)
  address=input("Enter Address of member : ")
  L.append(address)
  regfee=input("Enter the registration Fee : ")
  L.append(regfee)
  value=L
  sql="insert into club (enroll,sname,age,city,sportname,phone,address,regfee)values(%s,%s,%s,%s,%s,%s,%s,%s)"
  mycursor.execute(sql,value)
  mydb.commit()
def ClubView():
  def abcd():
    sql = "select * from club"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    print("Details about club are as follows:")
    print("registration number","name","age","city","sportname","phone no.","address","registration fee")
    for x in res:
      print (x)
  abcd()
def SearchClub():
   print("Please enter the details to view the fee details :")
   enroll=int(input("Enter the enroll number of the member whose fee is to be viewed : "))
   sql="Select * from club where enroll=%s"
   rl=(enroll,)
   mycursor.execute(sql,rl)
   res=mycursor.fetchall()
   if res==None:
     print("Record not Found . . . ")
     return
     print("The details of the memebrs are : " )
   for x in res:
     print(x)
def RemoveClub():
   enroll=int(input("Enter the enroll number of the memeber to be deleted : "))
   rl=(enroll,)
   sql="Delete from club where enroll=%s"
   mycursor.execute(sql,rl)
   mydb.commit()
def MenuSet(): #Function For The Memeber Management System
  print("Enter 1 : To Register Club")
  print("Enter 2 : To View Club ")
  print("Enter 3 : To Search Club ")
  print("Enter 4 : To Remove Club")
  # try: #Using Exceptions For Validation
  userInput = int(input("Please Select An Above Option: ")) #Will Take Input From User except ValueError:
  # exit("\nHy! That's Not A Number") #Error Message
  # finally:
  print("\n") #Print New Line
  if(userInput == 1):
   RegisterClub()
  elif (userInput==2):
   ClubView()
  elif (userInput==3):
   SearchClub()
  elif (userInput==4):
   RemoveClub()
  else:
   print("Enter correct choice. . . ")
def runAgain():
  runAgn = input("\nwant To Run Again Y/n: ")
  while(runAgn.lower() == 'y'):
     if(platform.system() == "Windows"):
       print(os.system('cls'))
     else:
       print(os.system('clear'))
MenuSet()
MenuSet()   
runAgain()

