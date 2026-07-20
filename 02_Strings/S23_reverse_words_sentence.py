# ==========================================================
# Question S23: Reverse Words in a Sentence
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# a sentence.
#
# Reverse the order of words in the sentence.
#
# Note:
# Do not reverse individual characters.
# Only reverse the position of words.
#
# Example:
#
# Input:
# Enter a Sentence: Python is easy
#
# Output:
#
# -------------------------
# Original Sentence : Python is easy
# Reversed Sentence : easy is Python
# -------------------------
# ==========================================================


sentence = input("Enter a Sentence: ")

words = sentence.split()

reverse_words = words[::-1]

reversed_sentence = " ".join(reverse_words)

print("Original Sentence :", sentence)
print("Reversed Sentence :", reversed_sentence)
