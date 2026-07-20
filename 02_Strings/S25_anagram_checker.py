# ==========================================================
# Question S25: Check Whether Two Strings are Anagrams
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# two strings.
#
# Check whether both strings are anagrams.
#
# Anagram:
# Two strings are anagrams if they contain the same
# characters with the same frequency but in a different
# order.
#
# Examples:
#
# Input:
# String 1: listen
# String 2: silent
#
# Output:
# Anagram
#
# Input:
# String 1: hello
# String 2: world
#
# Output:
# Not Anagram
#
# Rules:
# • Ignore spaces.
# • Ignore uppercase/lowercase differences.
#
# Display:
#
# • First String
# • Second String
# • Result
#
# Example:
#
# Enter First String: Listen
# Enter Second String: Silent
#
# -------------------------
# First String  : Listen
# Second String : Silent
# Result        : Anagram
# -------------------------
# ==========================================================


first_string = input("Enter First String: ")
second_string = input("Enter Second String: ")

# Remove spaces and convert to lowercase
first_string = first_string.replace(" ", "").lower()
second_string = second_string.replace(" ", "").lower()

# Compare sorted characters
if sorted(first_string) == sorted(second_string):
    result = "Anagram"
else:
    result = "Not Anagram"

print("First String  :", first_string)
print("Second String :", second_string)
print("Result        :", result)
