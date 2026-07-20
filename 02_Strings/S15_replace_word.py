# ==========================================================
# Question S15: Replace a Word in a String
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a sentence.
#
# Then ask the user to enter:
#
# • The word to be replaced
# • The new word
#
# Replace the specified word with the new word.
#
# Display:
#
# • Original Sentence
# • Updated Sentence
#
# Example:
#
# Enter a Sentence: I love Python
# Enter the Word to Replace: Python
# Enter the New Word: Java
#
# -------------------------
# Original Sentence : I love Python
# Updated Sentence  : I love Java
# -------------------------
# ==========================================================

sentence = input("Enter a Sentence: ")
old_word = input("Enter the Word to Replace: ")
new_word = input("Enter the New Word: ")

updated_sentence = sentence.replace(old_word, new_word)

print("updated sentence :",updated_sentence)