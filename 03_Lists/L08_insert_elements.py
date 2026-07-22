# ==========================================================
# Question L08: Insert Elements
# ----------------------------------------------------------
# Write a Python program that creates a list
# containing five numbers.
#
# Perform the following operations:
#
# • Insert 15 at index 1
# • Insert 35 at index 3
#
# Display:
#
# • Original List
# • Updated List
#
# Example:
#
# Numbers: [10, 20, 30, 40, 50]
#
# -------------------------
# Original List : [10, 20, 30, 40, 50]
# Updated List  : [10, 15, 20, 35, 30, 40, 50]
# -------------------------
# ==========================================================

Numbers=[10, 20, 30, 40, 50]
Numbers.insert(1, 15)
Numbers.insert(3, 35)

print("Updated List  :",Numbers)