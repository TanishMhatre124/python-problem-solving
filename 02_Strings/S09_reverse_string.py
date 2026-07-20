# ==========================================================
# Question S09: Reverse a String Using Slicing
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string.
#
# Reverse the entered string using string slicing.
#
# Display:
#
# • Entered String
# • Reversed String
#
# Note:
# Do not use loops or any built-in reverse functions.
# Use only string slicing.
#
# Example:
#
# Enter a String: Python
#
# -------------------------
# Entered String : Python
# Reversed String: nohtyP
# -------------------------
#
# Hint:
#
# string[::-1]
# ==========================================================


input=input("enter the string :")

print("reverse string  :",input[::-1])