# ==========================================================
# Question L11: Find Largest Element in a List
# ----------------------------------------------------------
# Write a Python program to find the largest element
# in a list without using max().
#
# Display:
#
# • Original List
# • Largest Element
#
# Example:
#
# Numbers: [45, 12, 78, 34, 90, 23]
#
# -------------------------
# Original List     : [45, 12, 78, 34, 90, 23]
# Largest Element   : 90
# -------------------------
# ==========================================================

numbers=[45, 12, 78, 34, 90, 23]

largest_number=numbers[0]
for num in numbers:
    if num > largest_number:
        largest_number=num

print("largest number is ",largest_number)            