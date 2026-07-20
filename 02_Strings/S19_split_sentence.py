# ==========================================================
# Question S19: Split a Sentence into Words
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a sentence.
#
# Split the sentence into individual words.
#
# Display:
#
# • Original Sentence
# • List of Words
#
# Example:
#
# Enter a Sentence: Python is easy to learn
#
# -------------------------
# Original Sentence : Python is easy to learn
# Words             : ['Python', 'is', 'easy', 'to', 'learn']
# -------------------------
# ==========================================================

original_sentence = input("Enter a original sentence: ")
list_of_words=original_sentence.split()
print("words :",list_of_words)