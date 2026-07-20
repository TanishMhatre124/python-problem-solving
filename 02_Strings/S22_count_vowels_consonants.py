# ==========================================================
# Question S22: Count Vowels and Consonants in a String
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string.
#
# Count the total number of:
#
# • Vowels (a, e, i, o, u)
# • Consonants (all other alphabet characters)
#
# Display:
#
# • Original String
# • Total Vowels
# • Total Consonants
#
# Rules:
#
# • Ignore spaces.
# • Ignore numbers and special characters.
# • Both uppercase and lowercase vowels should be counted.
#
# Example:
#
# Enter a String: Python Programming
#
# -------------------------
# Original String : Python Programming
# Vowels          : 4
# Consonants      : 12
# -------------------------
# ==========================================================

original_string = input("Enter the String: ")

vowels=0
consonants=0

for char in original_string:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1

print("Original String :", original_string)
print("Vowels          :", vowels)
print("Consonants      :", consonants)