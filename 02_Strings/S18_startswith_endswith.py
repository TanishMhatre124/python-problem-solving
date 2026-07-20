# ==========================================================
# Question S18: Check if a String Starts and Ends with
# a Specific Character or Word
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a string.
#
# Then ask the user to enter:
#
# • A starting character or word
# • An ending character or word
#
# Check whether the entered string:
#
# • Starts with the given starting character/word.
# • Ends with the given ending character/word.
#
# Display appropriate messages for both checks.
#
# Example:
#
# Enter a String: Python Programming
# Enter Starting Character/Word: Python
# Enter Ending Character/Word: ming
#
# -------------------------
# Starts With : True
# Ends With   : True
# -------------------------
# ==========================================================
sentence = input("Enter a String: ")
starting_word = input("Enter Starting Character/Word: ")
ending_word = input("Enter Ending Character/Word: ")

print("Starts With :", sentence.startswith(starting_word))
print("Ends With   :", sentence.endswith(ending_word))


#otherway
sentence = input("Enter a String: ")
starting_word = input("Enter Starting Character/Word: ")
ending_word = input("Enter Ending Character/Word: ")

if sentence.startswith(starting_word):
    print("Starts With : True")
else:
    print("Starts With : False")

if sentence.endswith(ending_word):
    print("Ends With   : True")
else:
    print("Ends With   : False")