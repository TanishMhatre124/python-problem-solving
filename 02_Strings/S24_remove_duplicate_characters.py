# ==========================================================
# Question S24: Remove Duplicate Characters from a String
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string.
#
# Remove all duplicate characters and keep only the
# first occurrence of each character.
#
# Display:
#
# • Original String
# • String after removing duplicates
#
# Example:
#
# Enter a String: programming
#
# -------------------------
# Original String : programming
# Result          : progamin
# -------------------------
#
# Note:
# The order of characters should remain the same.
# ==========================================================

# ==========================================================
# Question S24: Remove Duplicate Characters from a String
# ==========================================================

original_string = input("Enter a String: ")

result = ""

for char in original_string:
    if char not in result:
        result += char

print("Original String :", original_string)
print("Result          :", result)
