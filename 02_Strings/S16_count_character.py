# ==========================================================
# Question S16: Count the Number of Times a Character
# Appears in a String
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string.
#
# Then ask the user to enter a single character.
#
# Count how many times that character appears
# in the entered string.
#
# Display:
#
# • Original String
# • Character to Search
# • Number of Occurrences
#
# Example:
#
# Enter a String: programming
# Enter a Character: g
#
# -------------------------
# Original String      : programming
# Character Searched   : g
# Total Occurrences    : 2
# -------------------------
# ==========================================================


sentence = input("Enter the original string: ")
char_search = input("enter the( character: ")
total_occurance=sentence.count(char_search)

print("total occurance :", total_occurance)

