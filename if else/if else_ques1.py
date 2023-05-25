#Leap year questions
#for century year
#for not a century year

year = int(input("Enter a year : "))

if year%100 == 0:
    #a century year
    #we have to check for 400
    if year%400 == 0:
     print("Its a leap year")
    else:
       print("Its not a leap year")

else:
    #not a century year
    #we have to check for 4
    if year%4 == 0:
      print("Its a leap year")
    else:
       print("Its not a leap year")

