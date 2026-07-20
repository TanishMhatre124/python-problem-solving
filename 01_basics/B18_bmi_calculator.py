# ==========================================================
# Question 18: BMI Calculator
# ----------------------------------------------------------
# Write a Python program that asks the user to enter:
#
# • Weight (in kilograms)
# • Height (in meters)
#
# Calculate BMI using the formula:
#
# BMI = Weight / (Height × Height)
#
# Display:
#
# • Weight
# • Height
# • BMI
#
# Example:
#
# Enter Weight (kg): 70
# Enter Height (m): 1.75
#
# -------------------------
# Weight : 70 kg
# Height : 1.75 m
# BMI    : 22.86
# ==========================================================

weight=float(input("enter the weight :"))
height=float(input("enter the height :"))

bmi=weight/(height*height)

print("bmi is :", bmi)