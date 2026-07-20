# ==========================================================
# Question 28: Body Surface Area Calculator
# ----------------------------------------------------------
# Write a Python program that asks the user to enter:
#
# • Weight in kilograms
# • Height in centimeters
#
# Calculate Body Surface Area (BSA) using:
#
# BSA = √((Height × Weight) / 3600)
#
# Display:
#
# • Weight
# • Height
# • Body Surface Area
#
# Example:
#
# Enter Weight: 70
# Enter Height: 175
#
# -------------------------
# Weight : 70 kg
# Height : 175 cm
# BSA    : 1.84
# ==========================================================


import math

weight = float(input("Enter Weight in kg: "))
height = float(input("Enter Height in cm: "))

bsa = math.sqrt((height * weight) / 3600)

print("-------------------------")
print("Weight :", weight, "kg")
print("Height :", height, "cm")
print("BSA    :", bsa)
print("-------------------------")