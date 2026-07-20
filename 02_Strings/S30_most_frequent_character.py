# ==========================================================
# Question S30: Find the Most Frequent Character in a String
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string.
#
# Find the character that appears the most number of times.
#
# Ignore spaces and treat uppercase and lowercase letters
# as the same.
#
# Display:
#
# • Original String
# • Most Frequent Character
# • Frequency
#
# Example:
#
# Enter a String:
# Programming
#
# -------------------------
# Original String        : Programming
# Most Frequent Character: g
# Frequency              : 2
# -------------------------
#
# Note:
# If two characters have the same highest frequency,
# display the one that appears first in the string.
# ==========================================================



original_string = input("Enter a String: ")

frequency = {}

for char in original_string.lower():
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

most_frequent = ""
highest_count = 0

for char, count in frequency.items():
    if count > highest_count:
        highest_count = count
        most_frequent = char

print("Original String         :", original_string)
print("Most Frequent Character :", most_frequent)
print("Frequency               :", highest_count)
