weight=float(input("Enter your weight"))
unit=input("Kilogram or pounds?(Kg or L)")
if unit =="Kg":
    weight=weight*2.205
    print(f"Your weight  in kg is {weight}")
elif unit =="L":
    weight=weight/2.205
    print(f"Your weight in L is {weight}")
else:
    weight=invalid
print(f"Your weight is {weight}")