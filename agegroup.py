#wap to show the age group
age=int(input("enter your age:"))
if age>=0 and age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
else:
    print("Senior citizen")
    