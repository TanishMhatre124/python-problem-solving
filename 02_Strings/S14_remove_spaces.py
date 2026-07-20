# ==========================================================
# Question S14: Remove Leading and Trailing Spaces
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string with extra spaces at the beginning
# and at the end.
#
# Remove only the leading and trailing spaces
# from the entered string.
#
# Display:
#
# • Original String
# • String After Removing Extra Spaces
#
# Note:
# Spaces between words should remain unchanged.
#
# Example:
#
# Enter a String:     Hello Python Programming     
#
# -------------------------
# Original String :     Hello Python Programming     
# After Removing Spaces : Hello Python Programming
# -------------------------
# ==========================================================


n1=input("enter the string:")

print("original string is :",n1)
print("After Removing Spaces  IS :",n1.strip())
