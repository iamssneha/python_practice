age = int(input("Enter the age of person : "))
sex = input("Enter the sex of a personb M/F : ")
marital = input("Enter the marital status of a person Y/N : ")



if sex == 'F':
    print(" Female Work in urban area")
elif sex == 'M':
    if age>=20 and age<=40:
        print(" Person will work anywhere")
elif sex == 'M':
    if age>40 and age<60:
        print("Person will work in urban areas only")

else:
    print("ERROR")
  

    
