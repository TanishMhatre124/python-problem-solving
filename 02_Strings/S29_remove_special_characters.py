# ==========================================================
# Question S29: Remove Special Characters from a String
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string.
#
# Remove all special characters from the string.
#
# Keep only:
# • Alphabets (A-Z, a-z)
# • Numbers (0-9)
# • Spaces
#
# Display:
#
# • Original String
# • String after removing special characters
#
# Example:
#
# Enter a String:
# Hello@123! Welcome# to$ Python.
#
# -------------------------
# Original String : Hello@123! Welcome# to$ Python.
# Cleaned String  : Hello123 Welcome to Python
# -------------------------
#
# Note:
# Remove characters like:
# @ # $ % ^ & * ( ) ! ? . , : ; etc.
# ==========================================================


original_string = input("Enter a String: ")

cleaned_string = ""

for char in original_string:
    if char.isalnum() or char == " ":
        cleaned_string += char

print("Original String :", original_string)
print("Cleaned String  :", cleaned_string)
