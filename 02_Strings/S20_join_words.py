# ==========================================================
# Question S20: Join Words into a Sentence
# ----------------------------------------------------------
# Write a Python program that asks the user to enter
# multiple words separated by spaces.
#
# Convert the words into a list and join them back
# into a single sentence.
#
# Display:
#
# • Original Words
# • Joined Sentence
#
# Example:
#
# Enter Words: Python is easy to learn
#
# -------------------------
# Original Words   : ['Python', 'is', 'easy', 'to', 'learn']
# Joined Sentence  : Python is easy to learn
# -------------------------
# ==========================================================


# ==========================================================
# Question S20: Join Words into a Sentence
# ==========================================================

words = input("Enter Words: ")

word_list = words.split()

joined_sentence = " ".join(word_list)

print("Original Words  :", word_list)
print("Joined Sentence :", joined_sentence)
