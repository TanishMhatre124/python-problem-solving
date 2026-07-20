# ==========================================================
# Question S08: Display Different Parts of a String
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string.
#
# Using string slicing, display:
#
# • First 5 characters
# • Last 4 characters
# • Characters from index 2 to index 6
#
# Note:
# The ending index in slicing is NOT included.
#
# Example:
#
# Enter a String: PythonProgramming
#
# -------------------------
# Entered String        : PythonProgramming
# First 5 Characters    : Pytho
# Last 4 Characters     : ming
# Characters (2 to 6)   : thonP
# -------------------------
#
# Hint:
#
# string[:5]
# string[-4:]
# string[2:7]
# ==========================================================

input=input("enter the string :")

print("first 5  character :",input[:5])
print("last 4 character :",input[-4:])
print("characters(2 to 6):",input[2:6])