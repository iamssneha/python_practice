marks = int(input("Enter the marks of a student : "))

if marks>80:
    print("Grade A")
elif marks<=80 and marks>=60:
    print("Grade B")
elif marks<60 and marks>=50:
    print("Grade C")
elif marks<50 and marks>=45:
    print("Grade D")
elif marks<45 and marks>= 25:
    print("Grade E")

else:
    print("Fail")