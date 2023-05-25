age = int(input("Enter the age of person : "))
sex = int(input("Enter the sex of a personb M/F : "))
marital_status = int(input("Enter the marital status of a person : "))



if sex == 'F':
    print(" Female Work in urban area")
elif sex == 'M':
    if age>=20 & age<=40:
        print(" Person will work anywhere")
elif sex == 'M':
    if age>40 & age<60:
        print("Person will work in urban areas only")

else:
    print("ERROR")
  

    
