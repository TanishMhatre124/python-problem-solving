# ==========================================================
# Question 26: Calculate Area of Triangle
# ----------------------------------------------------------
# Write a Python program that asks the user to enter:
#
# • Base of Triangle
# • Height of Triangle
#
# Calculate the area using the formula:
#
# Area = (Base × Height) / 2
#
# Display:
#
# • Base
# • Height
# • Area of Triangle
#
# Example:
#
# Enter Base: 10
# Enter Height: 5
#
# -------------------------
# Base   : 10
# Height : 5
# Area   : 25
# ==========================================================


base = float(input("Enter Base of Triangle: "))
height = float(input("Enter Height of Triangle: "))

area = (base * height) / 2

print("-------------------------")
print("Base   :", base)
print("Height :", height)
print("Area   :", area)
print("-------------------------")