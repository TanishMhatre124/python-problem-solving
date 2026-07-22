# ==========================================================
# Question L12: Find Smallest Element in a List
# ----------------------------------------------------------
# Write a Python program to find the smallest element
# in a list without using min().
#
# Display:
#
# • Original List
# • Smallest Element
#
# Example:
#
# Numbers: [45, 12, 78, 34, 90, 23]
#
# -------------------------
# Original List     : [45, 12, 78, 34, 90, 23]
# Smallest Element  : 12
# -------------------------
# ==========================================================


numbers=[45, 12, 78, 34, 90, 23]

smallest_number=numbers[0]
for num in numbers:
    if num < smallest_number:
        smallest_number=num

print("smallest number is ",smallest_number)            