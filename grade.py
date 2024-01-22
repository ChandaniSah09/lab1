physics=int(input("enter the mark of physics:"))
biology=int(input("enter the mark of biology:"))
chemistry=int(input("enter the mark of chemistry:"))
average=(physics+biology+chemistry)/300*100
print(average,"is avegare")
if average>=90 and average<=100:
    print("Grade A")
elif average>=80 and average<=89:
    print("Grade B") 
elif average>=70 and average<=79:
    print("Grade C")

elif average>=60 and average<=69:
    print("Grade D")
else:
    print("Fail")
