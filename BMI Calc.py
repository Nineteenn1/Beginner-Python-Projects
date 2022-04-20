#This program Calculates BMI
print("BMI\n Less than 18.5 - Underweight\n 18.5–24.9 - Normal Weight\n 25–29.9 - Overweight\n 30 or more - Obesity")
Weight = float(input("Enter Your Weight (KG)"))
Height = float(input("Enter Your Height (CM)"))
BMI = Weight / (Height/100) **2
print(f"Your BMI is {BMI}")

