Height = float(input("Enter you height in cm: "))
Weight = float(input("Enter your weight in kg: "))

BMI = Height/Weight
if BMI<=18.4:
    print("You are underweight")
elif BMI<=24.9:
    print("You are Normal")
elif BMI<=29.9:
    print("You are overweight")
else:
    print("You are Obese")