# ==========================================================
# Question S21: Check Whether a String is Palindrome
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string.
#
# Check whether the entered string is a palindrome.
#
# A palindrome is a string that remains the same when
# reversed.
#
# Examples:
#
# Input: madam
# Output: Palindrome
#
# Input: python
# Output: Not Palindrome
#
# Display:
#
# • Original String
# • Result
#
# Example:
#
# Enter a String: madam
#
# -------------------------
# Original String : madam
# Result          : Palindrome
# -------------------------
# ==========================================================

original_string=input("enter a string :")

reverse_string=original_string[::-1]

if original_string==reverse_string:
    print(f"original string: {original_string}")
    print("result : palindrome")
else:
    print("result : not palindrome")
