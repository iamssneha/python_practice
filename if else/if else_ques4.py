num1 = int(input("Enter the age of 1st person : "))
num2 = int(input("Enter the age of 2nd person : "))
num3 = int(input("Enter the age of 3rd person : "))

if num1>num2 and num1>num3:
    print("num1 is oldest ")

    if num2>num1 and num2>num3:
      print("num2 is oldest ")

    if num3>num1 and num3>num2:
      print("num3 is oldest")

if num1<num2 and num1<num3:
    print("num1 is youngest ")

    if num2<num1 and num2<num3:
      print("num2 is youngest ")

    if num3<num1 and num3<num2:
      print("num3 is youngest")



