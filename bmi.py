weight=float(input("enter your weight :"))
height=float(input("enter your height :"))
BMI=weight/(height*height)
if BMI<18.5:
    print("Underweight")
elif BMI>=18.5 and BMI<=24.9:
    print("Normal Weight")
elif BMI>=25 and BMI<=29.9:
    print("Over weight")
elif BMI>=30:
    print("Obesity")
else:
    ("invalid input")