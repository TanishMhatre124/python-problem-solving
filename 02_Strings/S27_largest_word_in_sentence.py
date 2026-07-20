# ==========================================================
# Question S27: Find the Largest Word in a Sentence
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a sentence.
#
# Find the word with the maximum number of characters.
#
# Display:
#
# • Original Sentence
# • Largest Word
# • Length of Largest Word
#
# Example:
#
# Enter a Sentence: Python programming is very interesting
#
# -------------------------
# Original Sentence : Python programming is very interesting
# Largest Word      : programming
# Length            : 11
# -------------------------
#
# Note:
# If two words have the same length, display the first
# occurring word.
# ==========================================================


sentence = input("Enter a Sentence: ")

words = sentence.split()

largest_word = ""

for word in words:
    if len(word) > len(largest_word):
        largest_word = word

print("Original Sentence :", sentence)
print("Largest Word      :", largest_word)
print("Length            :", len(largest_word))