# ==========================================================
# Question S07: Display Characters Using Negative Indexing
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string.
#
# Display the following characters using negative indexing:
#
# • Last Character
# • Second Last Character
# • Third Last Character
#
# Note:
# Negative indexing starts from -1.
#
# Example:
#
# Enter a String: Python
#
# -------------------------
# Entered String      : Python
# Last Character      : n
# Second Last Character : o
# Third Last Character  : h
# -------------------------
#
# Hint:
# Use indexes:
#
# string[-1]
# string[-2]
# string[-3]
# ==========================================================

input=input("enter the string :")
print("last  character :",input[-1])
print("second last character :",input[-2])
print("third last character :",input[-3])
