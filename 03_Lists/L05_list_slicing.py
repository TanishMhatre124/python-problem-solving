# ==========================================================
# Question L05: List Slicing
# ----------------------------------------------------------
# Write a Python program that creates a list
# containing eight numbers.
#
# Display:
#
# • Complete List
# • First Three Elements
# • Last Three Elements
# • Middle Four Elements
#
# Example:
#
# Numbers: [10, 20, 30, 40, 50, 60, 70, 80]
#
# -------------------------
# Complete List      : [10, 20, 30, 40, 50, 60, 70, 80]
# First Three        : [10, 20, 30]
# Last Three         : [60, 70, 80]
# Middle Four        : [30, 40, 50, 60]
# -------------------------
# ==========================================================

numbers=[10, 20, 30, 40, 50, 60, 70, 80]
print("complete list :",numbers)
print("First Three: ",numbers[:3])
print("Last Three : ",numbers[-3:])
print("Middle Four :",numbers[2:6])
