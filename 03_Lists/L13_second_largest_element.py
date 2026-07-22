# ==========================================================
# Question L13: Find Second Largest Element in a List
# ----------------------------------------------------------
# Write a Python program to find the second largest
# element in a list without using sort() or max().
#
# Display:
#
# • Original List
# • Second Largest Element
#
# Example:
#
# Numbers: [45, 12, 78, 34, 90, 23]
#
# -------------------------
# Original List        : [45, 12, 78, 34, 90, 23]
# Second Largest      : 78
# -------------------------
# ==========================================================

numbers = [45, 12, 78, 34, 90, 23]

largest_number = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest_number:
        second_largest = largest_number
        largest_number = num

    elif num > second_largest:
        second_largest = num

print("Largest Number :", largest_number)
print("Second Largest :", second_largest)          
