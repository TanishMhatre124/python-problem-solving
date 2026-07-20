# ==========================================================
# Question S26: Count Frequency of Each Character in a String
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string.
#
# Count how many times each character appears in the string.
#
# Display:
#
# • Original String
# • Each character with its frequency
#
# Rules:
#
# • Ignore spaces.
# • Consider uppercase and lowercase as the same.
#
# Example:
#
# Enter a String: programming
#
# -------------------------
# Original String : programming
#
# Character Frequency:
# p : 1
# r : 2
# o : 1
# g : 2
# a : 1
# m : 2
# i : 1
# n : 1
# -------------------------
# ==========================================================


original_string = input("Enter a String: ")

frequency = {}

for char in original_string.lower():
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print("Original String :", original_string)

print("\nCharacter Frequency:")
for char, count in frequency.items():
    print(char, ":", count)