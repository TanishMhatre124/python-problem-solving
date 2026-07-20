# ==========================================================
# Question 12: Fahrenheit to Celsius Converter
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a temperature in Fahrenheit.
#
# Convert the temperature to Celsius using
# the formula:
#
# Celsius = (Fahrenheit - 32) × 5 / 9
#
# Display the converted temperature.
#
# Example:
#
# Enter temperature in Fahrenheit: 95
#
# Temperature in Celsius = 35.0
# ==========================================================


fahrenheit=float(input("enter the temperature in fahrenheit:"))
celsius= (fahrenheit - 32) * 5 / 9

print("Temperature in celsius =",celsius)
