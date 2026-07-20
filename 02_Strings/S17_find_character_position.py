# ==========================================================
# Question S17: Find the Position of a Character
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string.
#
# Then ask the user to enter a character.
#
# Find the position (index) of the first occurrence
# of that character in the string.
#
# Display:
#
# • Original String
# • Character to Search
# • Position of the Character
#
# Note:
# If the character is not found, display an
# appropriate message.
#
# Example 1:
#
# Enter a String: programming
# Enter a Character: g
#
# -------------------------
# Original String       : programming
# Character Searched    : g
# Position              : 3
# -------------------------
#
# Example 2:
#
# Enter a String: programming
# Enter a Character: z
#
# -------------------------
# Character not found.
# -------------------------
# ==========================================================


sentence = input("Enter the String: ")
char_search = input("Enter the Character: ")

position = sentence.find(char_search)

if position == -1:
    print("Character not found.")
else:
    print("Position of searched character:", position)