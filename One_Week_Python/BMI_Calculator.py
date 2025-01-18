weight = float(input("What is your weight (in pounds): "))
height = float(input("What is your height (in inches):"))

formula = (weight*703) / (height**2)
formula = round(formula, 1)

print(formula)

if formula <= 18.4:
    category = "Underweight."
elif formula <= 24.9:
    category = "Normal Weight."
elif formula <= 29.9:
    category = "OverWeight."
elif formula <= 34.9:
    category = "Moderately Obese."
elif formula <= 39.9:
    category = "Severely Obese."
else:
     category = "Morbidly Obese"
    
print(f"Your BMI is {formula}, you are {category}")
