# ==========================================================
# Question 15: Calculate the Average of Three Numbers
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# three numbers.
#
# Calculate the average using the formula:
#
# Average = (Number1 + Number2 + Number3) / 3
#
# Display:
#
# • First Number
# • Second Number
# • Third Number
# • Average
#
# Example:
#
# Enter First Number : 10
# Enter Second Number: 20
# Enter Third Number : 30
#
# -------------------------
# First Number  : 10
# Second Number : 20
# Third Number  : 30
# Average       : 20.0
# ==========================================================

number_1=float(input("Enter First Number :"))
number_2=float(input("Enter second Number :"))
number_3=float(input("Enter third  Number :"))

average=(number_1+number_2+number_3)/3

print("average:", average)