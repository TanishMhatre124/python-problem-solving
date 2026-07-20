# ==========================================================
# Question S28: Replace a Word in a Sentence
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a sentence.
#
# Replace a specific word with another word.
#
# Display:
#
# • Original Sentence
# • Word to Replace
# • New Word
# • Updated Sentence
#
# Example:
#
# Enter a Sentence: I love Python programming
#
# Enter Word to Replace: Python
#
# Enter New Word: Java
#
# -------------------------
# Original Sentence : I love Python programming
# Updated Sentence  : I love Java programming
# -------------------------
#
# Note:
# The replacement should happen wherever the word appears.
# ==========================================================

# ==========================================================
# Question S28: Replace a Word in a Sentence
# ==========================================================

sentence = input("Enter a Sentence: ")

old_word = input("Enter Word to Replace: ")

new_word = input("Enter New Word: ")

updated_sentence = sentence.replace(old_word, new_word)

print("Original Sentence :", sentence)
print("Updated Sentence  :", updated_sentence)
